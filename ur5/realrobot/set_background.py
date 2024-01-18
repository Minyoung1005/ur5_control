import os
import sys
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(FILE_PATH, '../ur5_mujoco'))
sys.path.append(os.path.join(FILE_PATH, '../object_wise/dqn'))

import argparse
from realur5_env import *
from real_sdf_module import SDFModule

import warnings
warnings.filterwarnings("ignore", category=UserWarning)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    # env config #
    parser.add_argument("--num_blocks", default=3, type=int)
    args = parser.parse_args()

    # env configuration #
    num_blocks = args.num_blocks

    convex_hull = False
    depth = False
    resize = True

    sdf_module = SDFModule(rgb_feature=True, resnet_feature=True, convex_hull=convex_hull, 
            binary_hole=True, using_depth=depth, tracker=None, resize=resize)
    ur5robot = UR5Robot()
    env = RealSDFEnv(ur5robot, sdf_module, num_blocks=num_blocks)

    background_img, _ = env.reset()
    plt.subplot(1, 2, 1)
    plt.imshow(background_img[0])
    plt.subplot(1, 2, 2)
    plt.imshow(background_img[1])
    plt.show()
    sdf_module.save_background(background_img[1])
    print("Saved the Image.")
