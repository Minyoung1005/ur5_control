import cv2
import numpy as np
from copy import deepcopy
from transform_utils import euler2quat, quat2mat

from segmentation_env import UR5Env, segmentation_env
from reward_functions import *

class mrcnn_env(segmentation_env):
    def __init__(self, ur5_env, num_blocks=1, mov_dist=0.05, max_steps=50, task=0, reward_type='binary', goal_type='pixel', seperate=False):
        super().__init__(ur5_env, num_blocks, mov_dist, max_steps, task, reward_type, seperate)
        self.goal_type = goal_type
        self.colors = np.array([[0.9, 0., 0.], 
                                [0., 0.9, 0.], 
                                [0., 0., 0.9]])
        if num_blocks==4:
            self.colors = np.array([[0.9, 0., 0.], 
                                    [0., 0.9, 0.], 
                                    [0., 0., 0.9],
                                    [0.93, 0.545, 0.93]])
                                    #[0.557, 0.357, 0.082]])
        if ur5_env.color:
            if ur5_env.xml_ver==2:
                self.colors = np.array([[1, 0.557, 0.03],
                                        [0.75, 0.0, 0.85],
                                        [0.0, 0.6, 1]])
            elif ur5_env.xml_ver==3:
                self.colors = np.array([[0.93, 0.545, 0.93],
                                        [0.527, 0.488, 0.075],
                                        [0.95, 0.25, 0.3]])

        scenario_goals = []
        scenario_goals.append([[0, 0.1], [0.07, 0.17], [-0.07, 0.03]])
        scenario_goals.append([[0.2, 0.3], [-0.2, 0.3], [0.2, -0.1]])
        scenario_goals.append([[0, 0.25], [0, 0.1], [0, -0.05]])
        scenario_goals.append([[-0.2, 0.22], [-0.13, 0.22], [-0.06, 0.22]])
        scenario_goals.append([[0.2, 0.2], [0.2, 0.15], [0.2, 0.1]])
        self.scenario_goals = np.array(scenario_goals)

    def set_target_with_color(self, color):
        # color: [R, G, B]
        target_obj= np.argmin(np.linalg.norm(self.colors - color, axis=1))
        self.set_target(target_obj)

    def init_env(self, scenario=None):
        self.env._init_robot()
        range_x = self.block_spawn_range_x
        range_y = self.block_spawn_range_y
        threshold = 0.10 #0.15

        if self.goal_type=='pixel':
            check_feasible = False
            while not check_feasible:
                self.goals = []
                init_poses = []
                goal_ims = []
                for obj_idx in range(self.num_blocks):
                    check_init_pos = False
                    check_goal_pos = False
                    if obj_idx < self.num_blocks:
                        while not check_goal_pos:
                            # check_goal_pos = True
                            gx = np.random.uniform(*range_x)
                            gy = np.random.uniform(*range_y)
                            check_goals = (obj_idx == 0) or (np.linalg.norm(np.array(self.goals) - np.array([gx, gy]), axis=1) > threshold).all()
                            if check_goals:
                                check_goal_pos = True
                        self.goals.append([gx, gy])
                        zero_array = np.zeros([self.env.camera_height, self.env.camera_width])
                        cv2.circle(zero_array, self.pos2pixel(gx, gy), 1, 1, -1)
                        goal_ims.append(zero_array)

                        while not check_init_pos:
                            # check_init_pos = True
                            tx = np.random.uniform(*range_x)
                            ty = np.random.uniform(*range_y)
                            check_inits = (obj_idx == 0) or (np.linalg.norm(np.array(init_poses) - np.array([tx, ty]), axis=1) > threshold).all()
                            check_overlap = (np.linalg.norm(np.array(self.goals) - np.array([tx, ty]), axis=1) > threshold).all()
                            if check_inits and check_overlap:
                                check_init_pos = True
                        init_poses.append([tx, ty])
                        tz = 0.9
                        self.env.sim.data.qpos[7*obj_idx+12: 7*obj_idx+15] = [tx, ty, tz]
                        x, y, z, w = euler2quat([0, 0, np.random.uniform(2*np.pi)])
                        self.env.sim.data.qpos[7*obj_idx+15: 7*obj_idx+19] = [w, x, y, z]

                    else:
                        self.env.sim.data.qpos[7*obj_idx + 12: 7*obj_idx + 15] = [0, 0, 0]
                self.env.sim.step()
                check_feasible = self.check_blocks_in_range()

            goal_image = np.concatenate(goal_ims)
            self.goal_image = goal_image.reshape([self.num_blocks, self.env.camera_height, self.env.camera_width])

        elif self.goal_type=='block':
            ## goal position ##
            check_feasible = False
            while not check_feasible:
                self.goals = []
                for obj_idx in range(self.num_blocks):
                    check_goal_pos = False
                    if obj_idx < self.num_blocks:
                        if scenario is not None:
                            gx, gy = self.scenario_goals[scenario][obj_idx]
                            gz = 0.9
                            x, y, z, w = euler2quat([0, 0, 0])
                        else:
                            while not check_goal_pos:
                                gx = np.random.uniform(*range_x)
                                gy = np.random.uniform(*range_y)
                                check_goals = (obj_idx == 0) or (np.linalg.norm(np.array(self.goals) - np.array([gx, gy]), axis=1) > threshold).all()
                                if check_goals:
                                    check_goal_pos = True
                            gz = 0.9
                            x, y, z, w = euler2quat([0, 0, np.random.uniform(2*np.pi)])
                        self.env.sim.data.qpos[7*obj_idx+12: 7*obj_idx+15] = [gx, gy, gz]
                        self.env.sim.data.qpos[7*obj_idx+15: 7*obj_idx+19] = [w, x, y, z]
                        self.goals.append([gx, gy])

                    else:
                        self.env.sim.data.qpos[7*obj_idx + 12: 7*obj_idx + 15] = [0, 0, 0]
                self.env.sim.step()
                check_feasible = self.check_blocks_in_range()
            self.goal_image = self.env.move_to_pos(self.init_pos, grasp=1.0)

            ## init position ##
            check_feasible = False
            while not check_feasible:
                init_poses = []
                for obj_idx in range(self.num_blocks):
                    check_init_pos = False
                    if obj_idx < self.num_blocks:
                        while not check_init_pos:
                            tx = np.random.uniform(*range_x)
                            ty = np.random.uniform(*range_y)
                            check_inits = (obj_idx == 0) or (np.linalg.norm(np.array(init_poses) - np.array([tx, ty]), axis=1) > threshold).all()
                            check_overlap = (np.linalg.norm(np.array(self.goals) - np.array([tx, ty]), axis=1) > threshold).all()
                            if check_inits and check_overlap:
                                check_init_pos = True
                        init_poses.append([tx, ty])
                        tz = 0.9
                        self.env.sim.data.qpos[7*obj_idx+12: 7*obj_idx+15] = [tx, ty, tz]
                        x, y, z, w = euler2quat([0, 0, np.random.uniform(2*np.pi)])
                        self.env.sim.data.qpos[7*obj_idx+15: 7*obj_idx+19] = [w, x, y, z]

                    else:
                        self.env.sim.data.qpos[7*obj_idx + 12: 7*obj_idx + 15] = [0, 0, 0]
                self.env.sim.step()
                check_feasible = self.check_blocks_in_range()

        im_state = self.env.move_to_pos(self.init_pos, grasp=1.0)
        self.step_count = 0
        return im_state

    def reset(self, scenario=None):
        if scenario is not None:
            scenario %= len(self.scenario_goals)
        im_state = self.init_env(scenario)
        return [im_state, self.goal_image]

    def step(self, action):
        pre_poses = []
        for obj_idx in range(self.num_blocks):
            pre_pos = deepcopy(self.env.sim.data.get_body_xpos('target_body_%d'%(obj_idx+1))[:2])
            pre_poses.append(pre_pos)

        px, py, theta_idx = action
        if theta_idx >= self.num_bins:
            print("Error! theta_idx cannot be bigger than number of angle bins.")
            exit()
        theta = theta_idx * (2*np.pi / self.num_bins)
        im_state, collision, contact, depth_state = self.push_from_pixel(px, py, theta)

        poses = []
        rotations = []
        for obj_idx in range(self.num_blocks):
            pos = deepcopy(self.env.sim.data.get_body_xpos('target_body_%d'%(obj_idx+1))[:2])
            poses.append(pos)
            quat = deepcopy(self.env.sim.data.get_body_xquat('target_body_%d'%(obj_idx+1)))
            rotation_mat = quat2mat(np.concatenate([quat[1:],quat[:1]]))
            rotations.append(rotation_mat[0][:2])

        info = {}
        info['seg_target'] = self.seg_target
        info['goals'] = np.array(self.goals)
        info['contact'] = contact
        info['collision'] = collision
        info['pre_poses'] = np.array(pre_poses)
        info['poses'] = np.array(poses)
        info['rotations'] = np.array(rotations)
        info['goal_flags'] = np.linalg.norm(info['goals']-info['poses'], axis=1) < self.threshold
        info['out_of_range'] = not self.check_blocks_in_range()

        reward, success, block_success = self.get_reward(info)
        info['success'] = success
        info['block_success'] = block_success

        self.step_count += 1
        done = success
        if self.step_count==self.max_steps:
            done = True

        goal_image = self.goal_image
        return [im_state, goal_image], reward, done, info


if __name__=='__main__':
    visualize = True
    env = UR5Env(render=True, camera_height=96, camera_width=96, control_freq=5, data_format='NHWC', xml_ver=0)
    ''''''
    ## saving background image ##
    # im = env.move_to_pos([0.0, -0.23, 1.4], grasp=1.0)
    # from PIL import Image
    # backim = Image.fromarray((255*im.transpose([1,2,0])).astype(np.uint8))
    # backim.save('background.png')

    env = segmentation_env(env, num_blocks=3, mov_dist=0.05, max_steps=100, reward_type='new')
    env.set_targets(2)

    state = env.reset()
    if visualize:
        fig = plt.figure()
        if env.task == 1:
            ax0 = fig.add_subplot(121)
            ax1 = fig.add_subplot(122)
        else:
            ax1 = fig.add_subplot(111)

        s0 = deepcopy(state[0]).transpose([1, 2, 0])
        if env.task == 1:
            if env.goal_type == 'pixel':
                s1 = np.zeros([env.env.camera_height, env.env.camera_width, 3])
                s1[:, :, :env.num_blocks] = state[1].transpose([1, 2, 0])
            else:
                s1 = deepcopy(state[1]).transpose([1, 2, 0])
            im0 = ax0.imshow(s1)
        im = ax1.imshow(s0)
        plt.show(block=False)
        fig.canvas.draw()
        fig.canvas.draw()

    for i in range(100):
        #action = [np.random.randint(6), np.random.randint(2)]
        try:
            action = input("Put action x, y, theta: ")
            action = [int(a) for a in action.split()]
            # action = [np.random.randint(10, 64), np.random.randint(10, 64), np.random.randint(8)]
        except KeyboardInterrupt:
            exit()
        except:
            continue
        if action[2] > 9:
            continue
        print('{} steps. action: {}'.format(env.step_count, action))
        states, reward, done, info = env.step(action)
        if visualize:
            s0 = deepcopy(state[0]).transpose([1, 2, 0])
            if env.task == 1:
                if env.goal_type == 'pixel':
                    s1 = np.zeros([env.env.camera_height, env.env.camera_width, 3])
                    s1[:, :, :env.num_blocks] = state[1].transpose([1, 2, 0])
                else:
                    s1 = deepcopy(state[1]).transpose([1, 2, 0])
                im0 = ax0.imshow(s1)
            s0[action[0], action[1]] = [1, 0, 0]
            im = ax1.imshow(s0)
            fig.canvas.draw()

        print('Reward: {}. Done: {}'.format(reward, done))
        if done:
            print('Done. New episode starts.')
            states = env.reset()
            if visualize:
                s0 = deepcopy(state[0]).transpose([1, 2, 0])
                if env.task == 1:
                    if env.goal_type == 'pixel':
                        s1 = np.zeros([env.env.camera_height, env.env.camera_width, 3])
                        s1[:, :, :env.num_blocks] = state[1].transpose([1, 2, 0])
                    else:
                        s1 = deepcopy(state[1]).transpose([1, 2, 0])
                    im0 = ax0.imshow(s1)
                s0[action[0], action[1]] = [1, 0, 0]
                im = ax1.imshow(s0)
                fig.canvas.draw()
