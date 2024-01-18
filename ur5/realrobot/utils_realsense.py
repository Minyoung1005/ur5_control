import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
import numpy as np
import pyrealsense2 as rs
import time


def _box(img, r):
    """ O(1) box filter
        img - >= 2d image
        r   - radius of box filter
    """
    (rows, cols) = img.shape[:2]
    imDst = np.zeros_like(img)


    tile = [1] * img.ndim
    tile[0] = r
    imCum = np.cumsum(img, 0)
    imDst[0:r+1, :, ...] = imCum[r:2*r+1, :, ...]
    imDst[r+1:rows-r, :, ...] = imCum[2*r+1:rows, :, ...] - imCum[0:rows-2*r-1, :, ...]
    imDst[rows-r:rows, :, ...] = np.tile(imCum[rows-1:rows, :, ...], tile) - imCum[rows-2*r-1:rows-r-1, :, ...]

    tile = [1] * img.ndim
    tile[1] = r
    imCum = np.cumsum(imDst, 1)
    imDst[:, 0:r+1, ...] = imCum[:, r:2*r+1, ...]
    imDst[:, r+1:cols-r, ...] = imCum[:, 2*r+1 : cols, ...] - imCum[:, 0 : cols-2*r-1, ...]
    imDst[:, cols-r: cols, ...] = np.tile(imCum[:, cols-1:cols, ...], tile) - imCum[:, cols-2*r-1 : cols-r-1, ...]

    return imDst


def _gf_color(I, p, r, eps, s=None):
    """ Color guided filter
    I - guide image (rgb)
    p - filtering input (single channel)
    r - window radius
    eps - regularization (roughly, variance of non-edge noise)
    s - subsampling factor for fast guided filter
    """
    fullI = I
    fullP = p
    if s is not None:
        I = sp.ndimage.zoom(fullI, [1/s, 1/s, 1], order=1)
        p = sp.ndimage.zoom(fullP, [1/s, 1/s], order=1)
        r = int(round(r / s))

    print('r', r)
    h, w = p.shape[:2]
    N = _box(np.ones((h, w)), r)

    mI_r = _box(I[:,:,0], r) / N
    mI_g = _box(I[:,:,1], r) / N
    mI_b = _box(I[:,:,2], r) / N

    mP = _box(p, r) / N

    # mean of I * p
    mIp_r = _box(I[:,:,0]*p, r) / N
    mIp_g = _box(I[:,:,1]*p, r) / N
    mIp_b = _box(I[:,:,2]*p, r) / N

    # per-patch covariance of (I, p)
    covIp_r = mIp_r - mI_r * mP
    covIp_g = mIp_g - mI_g * mP
    covIp_b = mIp_b - mI_b * mP

    # symmetric covariance matrix of I in each patch:
    #       rr rg rb
    #       rg gg gb
    #       rb gb bb
    var_I_rr = _box(I[:,:,0] * I[:,:,0], r) / N - mI_r * mI_r;
    var_I_rg = _box(I[:,:,0] * I[:,:,1], r) / N - mI_r * mI_g;
    var_I_rb = _box(I[:,:,0] * I[:,:,2], r) / N - mI_r * mI_b;

    var_I_gg = _box(I[:,:,1] * I[:,:,1], r) / N - mI_g * mI_g;
    var_I_gb = _box(I[:,:,1] * I[:,:,2], r) / N - mI_g * mI_b;

    var_I_bb = _box(I[:,:,2] * I[:,:,2], r) / N - mI_b * mI_b;

    a = np.zeros((h, w, 3))
    for i in range(h):
        for j in range(w):
            sig = np.array([
                [var_I_rr[i,j], var_I_rg[i,j], var_I_rb[i,j]],
                [var_I_rg[i,j], var_I_gg[i,j], var_I_gb[i,j]],
                [var_I_rb[i,j], var_I_gb[i,j], var_I_bb[i,j]]
            ])
            covIp = np.array([covIp_r[i,j], covIp_g[i,j], covIp_b[i,j]])
            a[i,j,:] = np.linalg.solve(sig + eps * np.eye(3), covIp)

    b = mP - a[:,:,0] * mI_r - a[:,:,1] * mI_g - a[:,:,2] * mI_b

    meanA = _box(a, r) / N[...,np.newaxis]
    meanB = _box(b, r) / N

    if s is not None:
        meanA = sp.ndimage.zoom(meanA, [s, s, 1], order=1)
        meanB = sp.ndimage.zoom(meanB, [s, s], order=1)

    q = np.sum(meanA * fullI, axis=2) + meanB

    return q


def _gf_gray(I, p, r, eps, s=None):
    """ grayscale (fast) guided filter
        I - guide image (1 channel)
        p - filter input (1 channel)
        r - window raidus
        eps - regularization (roughly, allowable variance of non-edge noise)
        s - subsampling factor for fast guided filter
    """
    if s is not None:
        Isub = sp.ndimage.zoom(I, 1/s, order=1)
        Psub = sp.ndimage.zoom(p, 1/s, order=1)
        r = round(r / s)
    else:
        Isub = I
        Psub = p


    (rows, cols) = Isub.shape

    N = _box(np.ones([rows, cols]), r)

    meanI = _box(Isub, r) / N
    meanP = _box(Psub, r) / N
    corrI = _box(Isub * Isub, r) / N
    corrIp = _box(Isub * Psub, r) / N
    varI = corrI - meanI * meanI
    covIp = corrIp - meanI * meanP


    a = covIp / (varI + eps)
    b = meanP - a * meanI

    meanA = box(a, r) / N
    meanB = box(b, r) / N

    if s is not None:
        meanA = sp.ndimage.zoom(meanA, s, order=1)
        meanB = sp.ndimage.zoom(meanB, s, order=1)

    q = meanA * I + meanB
    return q


def _gf_colorgray(I, p, r, eps, s=None):
    """ automatically choose color or gray guided filter based on I's shape """
    if I.ndim == 2 or I.shape[2] == 1:
        return _gf_gray(I, p, r, eps, s)
    elif I.ndim == 3 and I.shape[2] == 3:
        return _gf_color(I, p, r, eps, s)
    else:
        print("Invalid guide dimensions:", I.shape)


def _guided_filter(I, p, r, eps, s=None):
    """ run a guided filter per-channel on filtering input p
        I - guide image (1 or 3 channel)
        p - filter input (n channel)
        r - window raidus
        eps - regularization (roughly, allowable variance of non-edge noise)
        s - subsampling factor for fast guided filter
    """
    if p.ndim == 2:
        p3 = p[:,:,np.newaxis]

    out = np.zeros_like(p3)
    for ch in range(p3.shape[2]):
        out[:,:,ch] = _gf_colorgray(I, p3[:,:,ch], r, eps, s)
    return np.squeeze(out) if p.ndim == 2 else out


def frame_to_numpy(frame, dtype):
    arr = np.asanyarray(frame.get_data(), dtype=dtype)
    return arr


class RealSenseSensor():
    COLOR_IM_HEIGHT = 480
    COLOR_IM_WIDTH = 848 #640
    DEPTH_IM_HEIGHT = 480
    DEPTH_IM_WIDTH = 848 #640
    FPS = 30

    def __init__(self, cam_id):
        self._running = None
        # realsense objs
        self._id = cam_id
        self._pipe = rs.pipeline()
        self._cfg = rs.config()
        self._align = rs.align(rs.stream.color)

        # camera params
        self._depth_scale = None
        self._intrinsics = np.eye(3)
        self._color_intrinsics = np.eye(3)
        self._depth_intrinsics = np.eye(3)

        # post-processing filters
        self._colorizer = rs.colorizer()
        self._spatial_filter = rs.spatial_filter()
        self._hole_filling = rs.hole_filling_filter()
        self._temporal_filter = rs.temporal_filter()

    def _config_pipe(self):
        self._cfg.enable_device(self._id)
        # configure the color stream
        self._cfg.enable_stream(
            rs.stream.color,
            RealSenseSensor.COLOR_IM_WIDTH,
            RealSenseSensor.COLOR_IM_HEIGHT,
            rs.format.bgr8,
            RealSenseSensor.FPS
        )

        # configure the depth stream
        self._cfg.enable_stream(
            rs.stream.depth,
            RealSenseSensor.DEPTH_IM_WIDTH,
            #360 if self._depth_align else RealSenseSensor.DEPTH_IM_HEIGHT,
            RealSenseSensor.DEPTH_IM_HEIGHT,
            rs.format.z16,
            RealSenseSensor.FPS
        )

    def _set_depth_scale(self):
        sensor = self._profile.get_device().first_depth_sensor()
        self._depth_scale = sensor.get_depth_scale()

    def _set_color_intrinsics(self):
        strm = self._profile.get_stream(rs.stream.color)
        obj = strm.as_video_stream_profile().get_intrinsics()
        self._color_intrinsics[0, 0] = obj.fx
        self._color_intrinsics[1, 1] = obj.fy
        self._color_intrinsics[0, 2] = obj.ppx
        self._color_intrinsics[1, 2] = obj.ppy
        self._color_coeffs = obj.coeffs

    def _set_depth_intrinsics(self):
        strm = self._profile.get_stream(rs.stream.depth)
        obj = strm.as_video_stream_profile().get_intrinsics()
        self._depth_intrinsics[0, 0] = obj.fx
        self._depth_intrinsics[1, 1] = obj.fy
        self._depth_intrinsics[0, 2] = obj.ppx
        self._depth_intrinsics[1, 2] = obj.ppy
        self._depth_coeffs = obj.coeffs

    @property
    def get_K_D_color(self):
        return self._color_intrinsics, np.array(self._color_coeffs)

    @property
    def get_K_D_depth(self):
        return self._depth_intrinsics, np.array(self._depth_coeffs)

    def __del__(self):
        if self.is_running:
            self.stop()

    @property
    def is_running(self):
        return self._running

    def start(self):
        try:
            self._depth_align = True
            self._config_pipe()
            self._profile = self._pipe.start(self._cfg)

            # store intrinsics and depth scale
            self._set_depth_scale()
            self._set_color_intrinsics()
            self._set_depth_intrinsics()

            # skip 5 first frames
            for _ in range(5):
                self._pipe.wait_for_frames()

            self._running = True

        except RuntimeError as e:
            print(e)

    def stop(self):
        if not self._running:
            logging.warning('RealSense was not working.')
            return False
    
        self._pipe.stop()
        self._running = False
        return True

    def _read_color_depth_image(
            self, 
            apply_spatial=False, 
            apply_hole_filling=False, 
            apply_temporal=False,
            apply_guided_filter=False
            ):

        frames = self._pipe.wait_for_frames()
        if self._depth_align:
            frames = self._align.process(frames)

        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        if not depth_frame or not color_frame:
            logging.warning('Could not retrieve frames.')
            return None, None

        if apply_spatial:
            depth_frame = self._spatial_filter.process(depth_frame)
        if apply_hole_filling:
            depth_frame = self._hole_filling.process(depth_frame)
        if apply_temporal:
            depth_frame = self._temporal_filter.process(depth_frame)

        # convert to numpy arrays
        depth_image = frame_to_numpy(depth_frame, np.float32)
        color_image = frame_to_numpy(color_frame, np.uint8)

        # apply guided filter
        if apply_guided_filter:
            depth_image = self._guided_filter(color_image/255.0, depth_image, 10, 0.05)

        # convert depth to meters
        depth_image *= self._depth_scale

        # bgr to rgb
        color_image = color_image[..., ::-1]

        return color_image, depth_image

    def frames(self, spatial=False, hole_filling=False, temporal=False, guided_filter=False):
        if not self._running:
            self.start()
        #time.sleep(1.0)

        color_npy, depth_npy = self._read_color_depth_image(apply_spatial=spatial, apply_hole_filling=hole_filling, apply_temporal=temporal, apply_guided_filter=guided_filter)

        if self._running:
            self.stop()

        return color_npy, depth_npy
