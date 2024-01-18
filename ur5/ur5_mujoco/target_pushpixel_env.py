from ur5_env import *
from reward_functions import *
import cv2
import imageio
from transform_utils import euler2quat, quat2mat

class target_pushpixel_env(object):
    def __init__(self, ur5_env, num_blocks=1, mov_dist=0.05, max_steps=50, task=0, reward_type='binary', goal_type='circle', hide_goal=False, seperate=False):
        self.env = ur5_env 
        self.num_blocks = num_blocks
        self.num_bins = 8

        self.task = task # 0: Reach / 1: Push / 2: Push-feature
        self.mov_dist = mov_dist
        self.block_spawn_range_x = [-0.20, 0.20] #[-0.25, 0.25]
        self.block_spawn_range_y = [-0.10, 0.30] #[-0.15, 0.35]
        self.block_range_x = [-0.25, 0.25]
        self.block_range_y = [-0.15, 0.35]
        self.eef_range_x = [-0.35, 0.35]
        self.eef_range_y = [-0.22, 0.40]
        self.z_push = 1.05
        self.z_prepush = self.z_push + self.mov_dist
        self.z_collision_check = self.z_push + 0.025
        self.time_penalty = 0.02 #0.1
        self.max_steps = max_steps
        self.step_count = 0
        self.threshold = 0.05

        self.reward_type = reward_type
        self.goal_type = goal_type
        self.hide_goal = hide_goal
        self.seperate = seperate

        self.init_pos = [0.0, -0.23, 1.4]
        self.background_img = imageio.imread(os.path.join(file_path, 'background.png')) / 255.
        self.goals = []

        self.cam_id = 1
        self.cam_theta = 0.0 #30 * np.pi / 180
        # cam_mat = self.env.sim.data.get_camera_xmat("rlview")
        # cam_pos = self.env.sim.data.get_camera_xpos("rlview")

        self.colors = np.array([
            [0.9, 0.0, 0.0], [0.0, 0.9, 0.0], [0.0, 0.0, 0.9]
            # [0.6784, 1.0, 0.1843], [0.93, 0.545, 0.93], [0.9686, 0.902, 0]
            ])
        self.targets = [0, 1, 2]
        # self.init_env()
        # self.env.sim.forward()

    def set_targets(self, targets=[0, 1, 2]):
        self.targets = targets

    def get_reward(self, info):
        if self.task == 0:
            return reward_reach(self)
        elif self.seperate:
            if self.reward_type=="binary":
                return reward_binary_seperate(self, info)
            elif self.reward_type=="inverse":
                return reward_inverse_seperate(self, info)
            elif self.reward_type=="linear":
                return reward_linear_seperate(self, info)
            elif self.reward_type=="sparse":
                return reward_sparse_seperate(self, info)
            elif self.reward_type=="new":
                return reward_new_seperate(self, info)
        else:
            if self.reward_type=="binary":
                return reward_push_binary(self, info)
            elif self.reward_type=="inverse":
                return reward_push_inverse(self, info)
            elif self.reward_type=="linear":
                return reward_push_linear(self, info)
            elif self.reward_type=="sparse":
                return reward_push_sparse(self, info)
            elif self.reward_type=="new":
                return reward_push_new(self, info)

    def init_env(self):
        self.env._init_robot()
        range_x = self.block_spawn_range_x
        range_y = self.block_spawn_range_y
        threshold = 0.15

        if self.goal_type=='circle':
            check_feasible = False
            while not check_feasible:
                self.goal_image = deepcopy(self.background_img)
                self.goals = []
                init_poses = []
                for obj_idx in range(3):
                    check_init_pos = False
                    check_goal_pos = False
                    if obj_idx < self.num_blocks:
                        while not check_init_pos:
                            tx = np.random.uniform(*range_x)
                            ty = np.random.uniform(*range_y)
                            if obj_idx==0:
                                break
                            if (np.linalg.norm(np.array(init_poses) - np.array([tx, ty]), axis=1)>threshold).all():
                                check_init_pos = True
                        init_poses.append([tx, ty])
                        tz = 0.9
                        self.env.sim.data.qpos[7*obj_idx+12: 7*obj_idx+15] = [tx, ty, tz]
                        x, y, z, w = euler2quat([0, 0, np.random.uniform(2*np.pi)])
                        self.env.sim.data.qpos[7*obj_idx+15: 7*obj_idx+19] = [w, x, y, z]

                        if obj_idx not in self.targets:
                            gx, gy = tx, ty
                        else:
                            while not check_goal_pos:
                                gx = np.random.uniform(*range_x)
                                gy = np.random.uniform(*range_y)
                                if obj_idx==0:
                                    break
                                check_goals = (np.linalg.norm(np.array(self.goals) - np.array([gx, gy]), axis=1)>threshold).all()
                                check_inits = (np.linalg.norm(np.array(init_poses) - np.array([gx, gy]), axis=1)>threshold).all()
                                if check_goals and check_inits:
                                    check_goal_pos = True
                        self.goals.append([gx, gy])
                        cv2.circle(self.goal_image, self.pos2pixel(gx, gy), 1, self.colors[obj_idx], -1)
                        # self.goal_image[self.pos2pixel(*self.goal1)] = self.colors[0]
                        # px, py = self.block_range_x[0], self.block_range_y[0]
                        # cv2.circle(self.goal_image, self.pos2pixel(px, py), 1, [1,0,0], -1)

                    else:
                        self.env.sim.data.qpos[7*obj_idx + 12: 7*obj_idx + 15] = [0, 0, 0]
                self.env.sim.step()
                check_feasible = self.check_blocks_in_range()

            if self.env.data_format=='NCHW':
                self.goal_image = np.transpose(self.goal_image, [2, 0, 1])

        elif self.goal_type=='pixel':
            check_feasible = False
            while not check_feasible:
                self.goals = []
                init_poses = []
                goal_ims = []
                for obj_idx in range(3):
                    check_init_pos = False
                    check_goal_pos = False
                    if obj_idx < self.num_blocks:
                        while not check_init_pos:
                            tx = np.random.uniform(*range_x)
                            ty = np.random.uniform(*range_y)
                            if obj_idx == 0:
                                break
                            if (np.linalg.norm(np.array(init_poses) - np.array([tx, ty]), axis=1) > threshold).all():
                                check_init_pos = True
                        init_poses.append([tx, ty])
                        tz = 0.9
                        self.env.sim.data.qpos[7*obj_idx+12: 7*obj_idx+15] = [tx, ty, tz]
                        x, y, z, w = euler2quat([0, 0, np.random.uniform(2*np.pi)])
                        self.env.sim.data.qpos[7*obj_idx+15: 7*obj_idx+19] = [w, x, y, z]
                        if obj_idx not in self.targets:
                            gx, gy = tx, ty
                        else:
                            while not check_goal_pos:
                                gx = np.random.uniform(*range_x)
                                gy = np.random.uniform(*range_y)
                                if obj_idx == 0:
                                    break
                                check_goals = (np.linalg.norm(np.array(self.goals) - np.array([gx, gy]), axis=1) > threshold).all()
                                check_inits = (np.linalg.norm(np.array(init_poses) - np.array([gx, gy]), axis=1) > threshold).all()
                                if check_goals and check_inits:
                                    check_goal_pos = True
                        self.goals.append([gx, gy])
                        zero_array = np.zeros([self.env.camera_height, self.env.camera_width])
                        cv2.circle(zero_array, self.pos2pixel(gx, gy), 1, 1, -1)
                        goal_ims.append(zero_array)
                    else:
                        self.env.sim.data.qpos[7*obj_idx + 12: 7*obj_idx + 15] = [0, 0, 0]
                self.env.sim.step()
                check_feasible = self.check_blocks_in_range()

            goal_image = np.concatenate(goal_ims)
            self.goal_image = goal_image.reshape([self.num_blocks, self.env.camera_height, self.env.camera_width])
            if self.env.data_format=='NHWC':
                self.goal_image = np.transpose(self.goal_image, [1, 2, 0])

        im_state = self.env.move_to_pos(self.init_pos, grasp=1.0)
        self.step_count = 0
        return im_state

    def generate_goal(self, info):
        goal_flags = info['goal_flags']
        if self.goal_type == 'circle':
            goal_image = deepcopy(self.background_img)
            for i, goal in enumerate(self.goals):
                if goal_flags[i]:
                    continue
                gx, gy = goal
                cv2.circle(goal_image, self.pos2pixel(gx, gy), 1, self.colors[i], -1)
            if self.env.data_format == 'NCHW':
                goal_image = np.transpose(goal_image, [2, 0, 1])

        elif self.goal_type=='pixel':
            goal_ims = []
            for i, goal in enumerate(self.goals):
                gx, gy = goal
                zero_array = np.zeros([self.env.camera_height, self.env.camera_width])
                if not goal_flags[i]:
                    cv2.circle(zero_array, self.pos2pixel(gx, gy), 1, 1, -1)
                goal_ims.append(zero_array)
            goal_image = np.concatenate(goal_ims)
            goal_image = goal_image.reshape([self.num_blocks, self.env.camera_height, self.env.camera_width])
            if self.env.data_format=='NHWC':
                goal_image = np.transpose(goal_image, [1, 2, 0])

        elif self.goal_type=='block':
            goal_image = self.goal_image

        return goal_image

    def reset(self):
        # glfw.destroy_window(self.env.viewer.window)
        # self.env.viewer = None
        im_state = self.init_env()
        if self.task==0:
            return [im_state]
        elif self.task==1:
            return [im_state, self.goal_image]
        elif self.task==2:
            poses = []
            rotations = []
            for obj_idx in range(self.num_blocks):
                pos = deepcopy(self.env.sim.data.get_body_xpos('target_body_%d'%(obj_idx+1))[:2])
                poses.append(pos)
                quat = deepcopy(self.env.sim.data.get_body_xquat('target_body_%d'%(obj_idx+1)))
                rotation_mat = quat2mat(np.concatenate([quat[1:],quat[:1]]))
                rotations.append(rotation_mat[0][:2])
            poses = np.concatenate(poses)
            goals = np.concatenate(self.goals)
            rotations = np.concatenate(rotations)
            state = np.concatenate([poses, goals, rotations])
            return state


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
        im_state, collision, contact = self.push_from_pixel(px, py, theta)

        poses = []
        rotations = []
        for obj_idx in range(self.num_blocks):
            pos = deepcopy(self.env.sim.data.get_body_xpos('target_body_%d'%(obj_idx+1))[:2])
            poses.append(pos)
            quat = deepcopy(self.env.sim.data.get_body_xquat('target_body_%d'%(obj_idx+1)))
            rotation_mat = quat2mat(np.concatenate([quat[1:],quat[:1]]))
            rotations.append(rotation_mat[0][:2])

        info = {}
        info['targets'] = self.targets
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

        if self.seperate and type(reward) is float:
            reward = [reward] * self.num_blocks

        if self.task == 0:
            return [im_state], reward, done, info
        elif self.task == 1:
            if self.hide_goal:
                goal_image = self.generate_goal(info)
            else:
                goal_image = self.goal_image
            return [im_state, goal_image], reward, done, info
        elif self.task == 2:
            poses = info['poses'].flatten()
            goals = info['goals'].flatten()
            rotations = info['rotations'].flatten()
            state = np.concatenate([poses, goals, rotations])
            return state, reward, done, info

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
        for obj_idx in range(self.num_blocks):
            pos = self.env.sim.data.get_body_xpos('target_body_%d'%(obj_idx+1))[:2]
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

        x, y, z, w = euler2quat([np.pi, 0, -theta+np.pi/2])
        quat = [w, x, y, z]
        self.env.move_to_pos([pos_before[0], pos_before[1], self.z_prepush], quat, grasp=1.0)
        self.env.move_to_pos([pos_before[0], pos_before[1], self.z_collision_check], quat, grasp=1.0)
        force = self.env.sim.data.sensordata
        if np.abs(force[2]) > 1.0 or np.abs(force[5]) > 1.0:
            #print("Collision!")
            self.env.move_to_pos([pos_before[0], pos_before[1], self.z_prepush], quat, grasp=1.0)
            im_state = self.env.move_to_pos(self.init_pos, grasp=1.0)
            return im_state, True, np.zeros(self.num_blocks)

        self.env.move_to_pos([pos_before[0], pos_before[1], self.z_push], quat, grasp=1.0)
        self.env.move_to_pos_slow([pos_after[0], pos_after[1], self.z_push], quat, grasp=1.0)
        contacts = self.check_block_contacts()
        self.env.move_to_pos_slow([pos_after[0], pos_after[1], self.z_prepush], quat, grasp=1.0)
        im_state = self.env.move_to_pos(self.init_pos, grasp=1.0)
        return im_state, False, contacts

    def check_block_contacts(self):
        block_contacts = np.zeros(self.num_blocks)
        for i in range(self.env.sim.data.ncon):
            contact = self.env.sim.data.contact[i]
            geom1 = self.env.sim.model.geom_id2name(contact.geom1)
            geom2 = self.env.sim.model.geom_id2name(contact.geom2)
            if geom1 is None or geom2 is None: continue
            if 'target_' in geom1 and 'target_' in geom2:
                if max(int(geom1[-1]), int(geom2[-1])) > self.num_blocks:
                    continue
                block_contacts[int(geom1[-1])-1] = 1
                block_contacts[int(geom2[-1])-1] = 1
        return block_contacts 

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
        plt.imshow(frame.transpose([1,2,0]))
        plt.show()


if __name__=='__main__':
    visualize = True
    env = UR5Env(render=True, camera_height=96, camera_width=96, control_freq=5, data_format='NCHW', xml_ver=0)
    ''''''
    ## saving background image ##
    # im = env.move_to_pos([0.0, -0.23, 1.4], grasp=1.0)
    # from PIL import Image
    # backim = Image.fromarray((255*im.transpose([1,2,0])).astype(np.uint8))
    # backim.save('background.png')

    env = target_pushpixel_env(env, num_blocks=3, mov_dist=0.05, max_steps=100, task=1, reward_type='new', goal_type='circle')
    env.set_targets([2])

    # eef_range_x = [-0.3, 0.3]
    # eef_range_y = [-0.2, 0.4]
    print(env.pos2pixel(env.eef_range_x[0], env.eef_range_y[0]))
    print(env.pos2pixel(env.eef_range_x[0], env.eef_range_y[1]))
    print(env.pos2pixel(env.eef_range_x[1], env.eef_range_y[1]))
    print(env.pos2pixel(env.eef_range_x[1], env.eef_range_y[0]))
    print(env.pos2pixel(env.block_range_x[0], env.block_range_y[0]))
    print(env.pos2pixel(env.block_range_x[0], env.block_range_y[1]))
    print(env.pos2pixel(env.block_range_x[1], env.block_range_y[1]))
    print(env.pos2pixel(env.block_range_x[1], env.block_range_y[0]))

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
