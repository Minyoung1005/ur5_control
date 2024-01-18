from mujoco_py import load_model_from_path, MjSim, MjViewer
import mujoco_py
from transform_utils import euler2quat
from matplotlib import pyplot as plt
from PIL import Image
from copy import deepcopy
import numpy as np
import time

import os
file_path = os.path.dirname(os.path.abspath(__file__))

def show_image(img):
    #cv2.imshow("test", img)
    plt.figure(figsize = (16,9))
    plt.axis('off')
    plt.imshow(img)
    plt.show()

class Env():
    def __init__(
            self, 
            render=True,
            image_state=True,
            camera_height=64,
            camera_width=64,
            control_freq=8,
            data_format='NHWC',
	        camera_depth=False,
            camera_name='frontview',
            ):
        self.model_xml = 'make_urdf/objects.xml'
        self.render = render
        self.image_state = image_state
        self.camera_height = camera_height
        self.camera_width = camera_width
        self.data_format = data_format
        self.camera_depth = camera_depth
        self.camera_name = camera_name

        self.model = load_model_from_path(os.path.join(file_path, self.model_xml))

        self.n_substeps = 1  # 20
        self.sim = MjSim(self.model, nsubsteps=self.n_substeps)
        self.viewer = MjViewer(self.sim)
        self.viewer._hide_overlay = True
        # Camera pose
        lookat_refer = [0., 0., 0.9]  # self.sim.data.get_body_xpos('target_body_1')
        self.viewer.cam.lookat[0] = lookat_refer[0]
        self.viewer.cam.lookat[1] = lookat_refer[1]
        self.viewer.cam.lookat[2] = lookat_refer[2]
        self.viewer.cam.azimuth = 0  # -65 #-75 #-90 #-75
        self.viewer.cam.elevation = -30  # -30 #-60 #-15
        self.viewer.cam.distance = 2.0  # 1.5

        self.sim.forward()


    def get_im(self, camera_name):
        control_timestep = 1.
        cur_time = time.time()
        end_time = cur_time + control_timestep

        for i in range(100):
            self.sim.step()
            cur_time += self.sim.model.opt.timestep
            if self.render: self.sim.render(mode='window')
            else: self.sim.render(camera_name=camera_name, width=self.camera_width, height=self.camera_height, mode='offscreen')

        if self.render:
            self.viewer._set_mujoco_buffers()
            self.sim.render(camera_name=camera_name, width=self.camera_width, height=self.camera_height, depth=self.camera_depth, mode='offscreen')
            camera_obs = self.sim.render(camera_name=camera_name, width=self.camera_width, height=self.camera_height, depth=self.camera_depth, mode='offscreen')
            if self.camera_depth:
                im_rgb, im_depth = camera_obs
            else:
                im_rgb = camera_obs
            self.viewer._set_mujoco_buffers()
        else:
            self.sim.render(camera_name=camera_name, width=self.camera_width, height=self.camera_height, mode='offscreen')
            camera_obs = self.sim.render(camera_name=camera_name, width=self.camera_width, height=self.camera_height, depth=self.camera_depth, mode='offscreen')
            if self.camera_depth:
                im_rgb, im_depth = camera_obs
            else:
                im_rgb = camera_obs

        im_rgb = np.flip(im_rgb, axis=1) / 255.0
        if self.data_format=='NCHW':
            im_rgb = np.transpose(im_rgb, [2, 0, 1])

        if self.camera_depth:
            im_depth = np.flip(im_depth, axis=1)
            return im_rgb, im_depth
        else:
            return im_rgb


if __name__=='__main__':
    env = Env(camera_height=64, camera_width=64)
    x, y, z, w = euler2quat([0, 0, np.pi/3])

    for i in range(16):
        for o in range(16):
            env.sim.data.qpos[o * 7:o * 7 + 3] = [3, 3, 3]
        o = i%16
        env.sim.data.qpos[o*7:o*7+3] = [0, 0, 0]
        env.sim.data.qpos[o*7 + 3:o*7 + 7] = [w,x,y,z]
        for j in range(500):
            env.sim.step()
        im = env.get_im('frontview')
        img = Image.fromarray((im*255).astype(np.uint8))
        img.save('target_images/object_%d.png'%o)
        # plt.imshow(im)
        # plt.show
