from custom_geometric_transform import *

def world2cam(p, T_cam_to_world):
    if type(p) == list:
        p = np.array(p).reshape((len(p), 1))
    if p.shape[0] == 3:
        p = np.vstack((p, 1))
    p_cam = T_cam_to_world.dot(p)
    return p_cam[0:3, 0:1]

def cam2pixel(p, camera_intrinsics, distortion_coeffs=None):

    # Transform to camera normalized plane (z=1)
    p = p/p[2, 0]  # z=1

    # Distort point
    if distortion_coeffs is not None:
        p = distortPoint(p[0, 0], p[1, 0], distortion_coeffs)

    # Project to image plane
    pt_pixel_distort = camera_intrinsics.dot(p)
    return pt_pixel_distort[0:2, 0]

def pixel2cam(pixel, depth, camera_intrinsics, distortion_coeffs=None):
    pixel = np.vstack((pixel, 1))
    p = np.linalg.inv(camera_intrinsics).dot(pixel)*depth
    return p[0:2, 0]

def world2pixel(p, T_cam_to_world, camera_intrinsics, distortion_coeffs):
    return cam2pixel(world2cam(p, T_cam_to_world), camera_intrinsics, distortion_coeffs)

def distortPoint(x, y, distortion_coeffs):
    r2 = x*x + y*y
    r4 = r2*r2
    r6 = r4*r2
    d = distortion_coeffs
    k1, k2, p1, p2, k3 = d[0], d[1], d[2], d[3], d[4]
    x_distort = x * (1 + k1 * r2 + k2 * r4 + k3 * r6) + \
        2*p1*x*y + p2*(r2 + 2*x*x)
    y_distort = y * (1 + k1 * r2 + k2 * r4 + k3 * r6) + \
        p1*(r2 + 2*y*y) + 2*p2*x*y
    pt_cam_distort = np.array([[x_distort, y_distort, 1]]).transpose()
    return pt_cam_distort

def create_object_points(CHECKER_COLS, CHECKER_ROWS,square_size):
    objpoints = np.zeros((CHECKER_COLS*CHECKER_ROWS, 3), np.float32)
    objpoints[:, :2] = np.mgrid[0:CHECKER_ROWS, 0:CHECKER_COLS].T.reshape(-1, 2)
    objpoints[:, 0] -= (CHECKER_ROWS-1)/2.0
    objpoints[:, 1] -= (CHECKER_COLS-1)/2.0
    objpoints*=square_size
    return objpoints

def refineImageCorners(gray_image, corners):
    CRITERIA = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER + cv2.CALIB_CB_FAST_CHECK,
        100, 0.0005)
    grid_resolution = 7
    SIZE_OF_SEARCH_WINDOW=(grid_resolution, grid_resolution)
    HALF_SIZE_OF_ZERO_ZONE=(-1, -1)
    refined_corners = cv2.cornerSubPix(
        gray_image, corners, SIZE_OF_SEARCH_WINDOW, HALF_SIZE_OF_ZERO_ZONE, CRITERIA)
    return refined_corners

def get_chessboard_corners(img, CHECKER_COLS = 9,
                           CHECKER_ROWS = 6,
                           SQUARE_SIZE = 0.025):
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    flag_find_chessboard, corners = cv2.findChessboardCorners(gray, (CHECKER_ROWS, CHECKER_COLS), None)
    if not flag_find_chessboard:
        return None, None
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    objpoints=create_object_points(CHECKER_COLS, CHECKER_ROWS, SQUARE_SIZE)
    corners = refineImageCorners(gray, corners)
    return objpoints, corners

def isInRange(x, low, up):
    return x>=low and x<=up

def checkHSVColorType(color_value, color_type='r'):
    h, s, v=color_value[0], color_value[1], color_value[2]
    if color_type=='r':
        if (isInRange(h,0,20) or isInRange(h, 160, 180)) and isInRange(s,80,255) and isInRange(v,100,255):
            return True

    return False

def helperMakeUniqueChessboardFrame(img, R, p, SQUARE_SIZE, camera_intrinsics, distortion_coeffs):

    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    T=form_T(R,p)

    # -- 1. Make chessboard z axis pointing towards the camera
    vec_cam_to_chess = np.array(p).squeeze(axis=1)
    vec_chess_z = T.dot(np.array([[0],[0],[1],[0]])).squeeze(axis=1)[0:3]-np.array(p)
    if np.sum(vec_cam_to_chess*vec_chess_z)>0:
        T=T.dot(rotx(np.pi, matrix_len=4))

    # -- 2. A manually drawn dot at required pos.
    def compute_mean_gray(pdot_chess_frame):
        pdot_pixel=world2pixel(pdot_chess_frame, T, camera_intrinsics, distortion_coeffs)
        RADIUS=0
        u,v=int(pdot_pixel[0]), int(pdot_pixel[1])
        cnt_red=0
        for i in range(-RADIUS,+RADIUS+1):
            for j in range(-RADIUS,+RADIUS+1):
                r,c=v+i,u+j
                # print img_hsv[r][c]
                if checkHSVColorType(img_hsv[r][c],'r'):
                    cnt_red+=1
        return cnt_red
    # print "side 1:",
    pdot_chess1=[0.5*SQUARE_SIZE, -0.5*SQUARE_SIZE, 0]
    cnt_red1=compute_mean_gray(pdot_chess1)
    # print "side 2:",
    pdot_chess2=[-0.5*SQUARE_SIZE, +0.5*SQUARE_SIZE, 0]
    cnt_red2=compute_mean_gray(pdot_chess2)
    # print cnt_red1, cnt_red2
    if cnt_red1>cnt_red2:
        T=T.dot(rotz(np.pi,matrix_len=4))

    # -- Return
    R, p = get_Rp_from_T(T)
    return R,p

