import copy
import sys
sys.path.append('/usr/lib/python2.7/dist-packages')
import rospy

from utils_realsense import RealSenseSensor
from calibration_helper import *
from matplotlib import pyplot as plt

from transformations import quaternion_matrix
from transformations import quaternion_from_matrix
from transformations import rotation_matrix
from transform_utils import euler2quat
from sklearn.cluster import SpectralClustering

# ros related packages
from ur_msgs.srv import JointTrajectory, EndPose, JointStates

# calibration
sys.path.append('/home/dof6/Desktop/Pose-Estimation-for-Sensor-Calibration')
from axxb_solver import *
from Pose_Estimation_Class import *


def inverse_projection(depth_img, pixel, K_realsense, D_realsense):
    depth = depth_img[pixel[1], pixel[0]]
    point = pixel2cam(pixel.reshape([-1,1]), depth, K_realsense, D_realsense)
    return np.array([point[0], point[1], depth])

def get_input_rgbd_image(realsense,
                         crop_size = 430,
                         resize_width = 256,
                         resize_height = 256):
    realsense.stop()
    realsense.start()
    rospy.sleep(0.2)
    rgb_im, depth_im, hole_mask = realsense._read_color_and_depth_image(apply_hole_filling=True,apply_temporal=False)
    realsense.stop()
    
    midx, midy = realsense._intrinsics[:2,2]
    input_rgb_im = resize_image(crop_image(rgb_im, midx, midy, crop_size), resize_width, resize_height)
    input_depth_im = resize_image(crop_image(depth_im, midx, midy, crop_size), resize_width, resize_height)
    input_hole_mask = resize_image(crop_image(hole_mask, midx, midy, crop_size), resize_width, resize_height)
    return input_rgb_im, input_depth_im, input_hole_mask, rgb_im, depth_im, hole_mask

def crop_image(image, midx, midy, crop_size=430):
    cs = crop_size
    cropped_image = image[int(np.round(midy-cs/2)):int(np.round(midy+cs/2)), int(np.round(midx-cs/2)):int(np.round(midx+cs/2))]
    return cropped_image

def resize_image(image, resize_width=256, resize_height=256):
    return cv2.resize(image, (resize_width, resize_height), interpolation=cv2.INTER_AREA)

def scaling_segmask(segmask,
                    realsense,
                    crop_size = 430,
                    resize_width = 256,
                    resize_height = 256):

    midx, midy = realsense._intrinsics[:2,2]
    input_segmask = resize_image(crop_image(segmask, midx, midy, crop_size), resize_width, resize_height)
    return input_segmask

def inverse_raw_pixel(pixel, midx, midy, cs=430, ih=256, iw=256):
    pixel = pixel * float(cs)/float(ih)
    px = int(pixel[0] + midx - cs/2.)
    py = int(pixel[1] + midy - cs/2.)
    return np.array([px, py])

def map_pixel(pixel, midx, midy, cs=430, ih=256, iw=256):
    pixel[0] = pixel[0] - midx + cs/2.
    pixel[1] = pixel[1] - midy + cs/2.
    pixel = pixel * float(ih)/float(cs)
    px, py = int(round(pixel[0])), int(round(pixel[1]))
    return np.array([px, py])
