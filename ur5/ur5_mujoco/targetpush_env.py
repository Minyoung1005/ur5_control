import numpy as np

from ur5_env import *
from reward_functions import *
import imageio
import cv2
from transform_utils import euler2quat

class targetpush_env(object):
    def __init__(self, ur5_env, num_use=16, num_select=4, mov_dist=0.10, max_steps=50, task=0):
        self.env = ur5_env
        self.num_total_blocks = 16
        self.num_use = num_use
        self.num_select = num_select

        self.task = task  # 0: Touch / 1: Push
        self.num_bins = 8
        self.mov_dist = mov_dist
        self.block_range_x = [-0.25, 0.25]
        self.block_range_y = [-0.15, 0.35]
        self.eef_range_x = [-0.3, 0.3]
        self.eef_range_y = [-0.2, 0.4]
        self.z_push = 1.05
        self.z_prepush = self.z_push + self.mov_dist
        self.z_collision_check = self.z_push + 0.025
        self.time_penalty = 0.02 #0.1
        self.max_steps = max_steps
        self.step_count = 0
        self.threshold = 0.05

        self.init_pos = [0.0, -0.23, 1.4]

        self.cam_id = 1
        self.cam_theta = 30 * np.pi / 180
        # cam_mat = self.env.sim.data.get_camera_xmat("rlview")
        # cam_pos = self.env.sim.data.get_camera_xpos("rlview")

        self.object_images = self.load_object_images()

        self.colors = np.array([ 
            [0.6784, 1.0, 0.1843], 
            [0.93, 0.545, 0.93], 
            [0.9686, 0.902, 0] 
            ])

        self.init_env()

    def load_object_images(self):
        obj_ims = []
        for obj in range(self.num_total_blocks):
            obj_im = imageio.imread(os.path.join(file_path, '../ur5_mujoco', 'target_images/object_%d.png'%obj))
            obj_ims.append(obj_im)
        return obj_ims

    def get_reward(self, info):
        if self.task == 0:
            return reward_touch(self, info)
        elif self.task == 1:
            return reward_targetpush(self, info)

    def init_env(self, target=-1):
        self.env._init_robot()
        range_x = self.block_range_x
        range_y = self.block_range_y
        assert self.num_select <= self.num_use <= self.num_total_blocks

        if self.task==1:
            if target==-1:
                self.selected = np.random.choice(range(self.num_use), \
                                                 self.num_select, replace=False)
                self.target_obj = np.random.choice(self.selected)
            else:
                self.target_obj = target
                self.selected = np.random.choice(range(self.num_use), \
                                                 self.num_select-1, replace=False)
                self.selected = np.concatenate([[self.target_obj], self.selected])

            self.goal_image = self.object_images[self.target_obj]

        x = np.linspace(range_x[0]+0.05, range_x[1]-0.05, 11)
        y = np.linspace(range_y[1]-0.05, range_y[0]+0.05, 11)
        xx, yy = np.meshgrid(x, y, sparse=True)

        check_feasible = False
        while not check_feasible:
            px = np.random.choice(range(11), self.num_select, False)
            py = np.random.choice(range(11), self.num_select, False)
            try:
                i = 0
                for obj_idx in range(self.num_total_blocks):
                    if obj_idx in self.selected:
                        tx = xx[0][px[i]]
                        ty = yy[py[i]][0]
                        while self.task==1 and np.linalg.norm([tx, ty]) < 0.10:
                            tx = np.random.uniform(*range_x)
                            ty = np.random.uniform(*range_y)
                        i += 1
                        tz = 0.9
                        self.env.sim.data.qpos[7*obj_idx + 12: 7*obj_idx + 15] = [tx, ty, tz]
                        x, y, z, w = euler2quat([0, 0, np.random.uniform(2*np.pi)])
                        self.env.sim.data.qpos[7*obj_idx + 15: 7*obj_idx + 19] = [w, x, y, z]
                    else:
                        self.env.sim.data.qpos[7*obj_idx + 12: 7*obj_idx + 15] = [0, 0, 0]
                self.env.sim.step()
                check_feasible = self.check_blocks_in_range()
            except:
                continue


        im_state = self.env.move_to_pos(self.init_pos, grasp=1.0)
        if self.task==1 and self.env.data_format=='NCHW':
            self.goal_image = np.transpose(self.goal_image, [2, 0, 1])
        self.step_count = 0

        return im_state

    def reset(self, target=-1):
        im_state = self.init_env(target)
        if self.task==0:
            return [im_state]
        else:
            return [im_state, self.goal_image]

    def step(self, action):
        pre_poses = []
        for obj_idx in self.selected:
            pre_pos = deepcopy(self.env.sim.data.get_body_xpos('object_%d'%obj_idx)[:2])
            pre_poses.append(pre_pos)

        px, py, theta_idx = action
        if theta_idx >= self.num_bins:
            print("Error! theta_idx cannot be bigger than number of angle bins.")
            exit()
        theta = theta_idx * (2*np.pi / self.num_bins)
        im_state, collision = self.push_from_pixel(px, py, theta)

        poses = []
        for obj_idx in self.selected:
            pos = deepcopy(self.env.sim.data.get_body_xpos('object_%d'%obj_idx)[:2])
            poses.append(pos)

        info = {}
        info['obj_indices'] = self.selected
        info['collision'] = collision
        info['pre_poses'] = np.array(pre_poses)
        info['poses'] = np.array(poses)
        if self.task==1:
            info['target_obj'] = self.target_obj

        reward, done = self.get_reward(info)
        # info['success'] = success
        if collision:
            reward = -0.1

        self.step_count += 1
        if self.step_count==self.max_steps:
            done = True
        if not self.check_blocks_in_range():
            #print("blocks not in feasible area.")
            reward = -1.
            done = True

        if self.task == 0:
            return [im_state], reward, done, info
        else:
            return [im_state, self.goal_image], reward, done, info

    def clip_pos(self, pose):
        x, y = pose
        range_x = self.eef_range_x
        range_y = self.eef_range_y
        x = np.max((x, range_x[0]))
        x = np.min((x, range_x[1]))
        y = np.max((y, range_y[0]))
        y = np.min((y, range_y[1]))
        return x, y

    def check_blocks_in_range(self):
        poses = []
        for obj_idx in self.selected:
            pos = self.env.sim.data.get_body_xpos('object_%d'%obj_idx)[:2]
            poses.append(pos)
        x_max, y_max = np.concatenate(poses).reshape(-1, 2).max(0)
        x_min, y_min = np.concatenate(poses).reshape(-1, 2).min(0)
        if x_max > self.block_range_x[1] or x_min < self.block_range_x[0]:
            return False
        if y_max > self.block_range_y[1] or y_min < self.block_range_y[0]:
            return False
        return True

    def push_from_pixel(self, px, py, theta):
        pos_before = np.array(self.pixel2pos(px, py))
        pos_before[:2] = self.clip_pos(pos_before[:2])
        pos_after = pos_before + self.mov_dist * np.array([np.sin(theta), np.cos(theta), 0.])
        pos_after[:2] = self.clip_pos(pos_after[:2])

        self.env.move_to_pos([pos_before[0], pos_before[1], self.z_prepush], grasp=1.0)
        self.env.move_to_pos([pos_before[0], pos_before[1], self.z_collision_check], grasp=1.0)
        force = self.env.sim.data.sensordata
        if np.abs(force[2]) > 1.0 or np.abs(force[5]) > 1.0:
            # print("Collision!")
            self.env.move_to_pos([pos_before[0], pos_before[1], self.z_prepush], grasp=1.0)
            im_state = self.env.move_to_pos(self.init_pos, grasp=1.0)
            return im_state, True
        self.env.move_to_pos([pos_before[0], pos_before[1], self.z_push], grasp=1.0)
        self.env.move_to_pos([pos_after[0], pos_after[1], self.z_push], grasp=1.0)
        self.env.move_to_pos([pos_after[0], pos_after[1], self.z_prepush], grasp=1.0)
        im_state = self.env.move_to_pos(self.init_pos, grasp=1.0)
        return im_state, False

    def pixel2pos(self, v, u): # u, v
        theta = self.cam_theta
        cx, cy, cz = self.env.sim.model.cam_pos[self.cam_id]
        fovy = self.env.sim.model.cam_fovy[self.cam_id]
        f = 0.5 * self.env.camera_height / np.tan(fovy * np.pi / 360)
        u0 = 0.5 * self.env.camera_width
        v0 = 0.5 * self.env.camera_height
        z0 = 0.9  # table height
        y_cam = (cz - z0) / (np.sin(theta) + np.cos(theta) * f / (v - v0 + 1e-10))
        x_cam = (u - u0) / (v - v0 + 1e-10) * y_cam
        x = - x_cam
        y = np.tan(theta) * (z0 - cz) + cy + 1 / np.cos(theta) * y_cam
        z = z0
        # print("cam pos:", [x_cam, y_cam])
        # print("world pos:", [x, y])
        # print()
        return x, y, z

    def pos2pixel(self, x, y):
        theta = self.cam_theta
        cx, cy, cz = self.env.sim.model.cam_pos[self.cam_id]
        fovy = self.env.sim.model.cam_fovy[self.cam_id]
        f = 0.5 * self.env.camera_height / np.tan(fovy * np.pi / 360)
        u0 = 0.5 * self.env.camera_width
        v0 = 0.5 * self.env.camera_height
        z0 = 0.9  # table height
        y_cam = np.cos(theta) * (y - cy - np.tan(theta) * (z0 - cz))
        dv = f * np.cos(theta) / ((cz - z0) / y_cam - np.sin(theta))
        v = dv + v0
        u = - dv * x / y_cam + u0
        return int(u), int(v)

    def move2pixel(self, u, v):
        target_pos = np.array(self.pixel2pos(u, v))
        target_pos[2] = 1.05
        frame = self.env.move_to_pos(target_pos)
        plt.imshow(frame)
        plt.show()


if __name__=='__main__':
    visualize = True
    task = 1
    xml_ver = task + 1
    env = UR5Env(render=True, camera_height=64, camera_width=64, control_freq=5, data_format='NHWC', xml_ver=xml_ver)
    env = targetpush_env(env, mov_dist=0.10, max_steps=100, task=task)

    states = env.reset()
    if visualize:
        fig = plt.figure()
        if task == 1:
            ax = fig.add_subplot(121)
            ax.imshow(states[0])
            ax2 = fig.add_subplot(122)
            ax2.imshow(states[1])
        else:
            ax = fig.add_subplot(111)
            ax.imshow(states[0])
        plt.show(block=False)
        fig.canvas.draw()
        fig.canvas.draw()

    for i in range(100):
        # action = [np.random.randint(6), np.random.randint(2), np.random.randint]
        try:
            # action = input("Put action x, y, theta: ")
            # action = [int(a) for a in action.split()]
            action = [np.random.randint(10, 64), np.random.randint(10, 64), np.random.randint(8)]
        except KeyboardInterrupt:
            exit()
        except:
            continue
        if action[2] > 9:
            continue
        print('{} steps. action: {}'.format(env.step_count, action))
        states, reward, done, info = env.step(action)
        if visualize:
            ax.imshow(states[0])
            if task==1:
                ax2.imshow(states[1])
            fig.canvas.draw()

        print('Reward: {}. Done: {}'.format(reward, done))
        if done:
            print('Done. New episode starts.')
            states = env.reset()
            if visualize:
                ax.imshow(states[0])
                if task==1:
                    ax2.imshow(states[1])
                fig.canvas.draw()
