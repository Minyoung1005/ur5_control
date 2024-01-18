import cv2
from ur5_env import *
from reward_functions import *
from transform_utils import euler2quat, quat2mat

class continuous_env(object):
    def __init__(self, ur5_env, num_blocks=1, mov_dist=0.03, max_steps=50, task=1, state='feature', reward_type='new'):
        self.env = ur5_env
        self.num_blocks = num_blocks

        self.task = task # 0: Reach / 1: Push / 2: Pick / 3: Place
        if self.task==0:
            self.action_dim = 2 # x, y
        elif self.task==1:
            self.action_range = 2 # x, y
        else:
            self.action_range = 3 # x, y, z

        self.mov_dist = mov_dist
        self.state_type = state
        self.reward_type = reward_type

        self.block_spawn_range_x = [-0.20, 0.20]
        self.block_spawn_range_y = [-0.10, 0.30]
        self.block_range_x = [-0.25, 0.25]
        self.block_range_y = [-0.15, 0.35]
        self.eef_range_x = [-0.35, 0.35]
        self.eef_range_y = [-0.22, 0.40]
        self.z_min = 1.05
        self.z_max = self.z_min + 3 * self.mov_dist
        self.z_push = self.z_min + 0.015
        self.time_penalty = 1e-2
        self.max_steps = max_steps
        self.step_count = 0
        self.threshold = 0.05

        if self.task < 2:
            self.init_pos = [0.0, 0.1, self.z_push]
        else:
            self.init_pos = [0.0, 0.1, self.z_min + self.mov_dist]
        self.init_env()

    def init_env(self):
        self.env._init_robot()
        range_x = self.block_spawn_range_x
        range_y = self.block_spawn_range_y
        threshold = 0.12

        check_feasible = False
        while not check_feasible:
            #self.goal_image = deepcopy(self.background_img)
            self.goals = []
            init_poses = []
            for obj_idx in range(3):
                check_init_pos = False
                check_goal_pos = False
                if obj_idx < self.num_blocks:
                    while not check_goal_pos:
                        gx = np.random.uniform(*range_x)
                        gy = np.random.uniform(*range_y)
                        if obj_idx==0:
                            break
                        check_goals = (obj_idx == 0) or (np.linalg.norm(np.array(self.goals) - np.array([gx, gy]), axis=1) > threshold).all()
                        if check_goals:
                            check_goal_pos = True
                    self.goals.append([gx, gy])
                    #cv2.circle(self.goal_image, self.pos2pixel(gx, gy), 1, self.colors[obj_idx], -1)
                    while not check_init_pos:
                        tx = np.random.uniform(*range_x)
                        ty = np.random.uniform(*range_y)
                        if obj_idx==0:
                            break
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
        for gi, goal_pose in enumerate(self.goals):
            self.env.sim.model.body_pos[20 + gi][:2] = goal_pose
            self.env.sim.model.body_pos[20 + gi][2] = 0.87
        im_state = self.env.move_to_pos(self.init_pos, grasp=1.0)
        self.step_count = 0
        return im_state

    def reset(self):
        im_state = self.init_env()
        if self.state_type=='feature':
            gripper_pos, grasp = self.get_gripper_state()
            block_poses, _ = self.get_poses()
            gripper_pos = np.array(gripper_pos).flatten()
            block_poses = np.array(block_poses).flatten()
            goal_poses = np.array(self.goals).flatten()
            if self.task==0:
                return np.concatenate([gripper_pos, block_poses])
            elif self.task==1:
                return np.concatenate([gripper_pos, block_poses, goal_poses])
            else:
                return np.concatenate([gripper_pos, block_poses, goal_poses, [grasp]])
        else:
            if self.task==0:
                return im_state, gripper_height
            else:
                return im_state, self.goal_image, gripper_height

    def step(self, action):
        pre_gripper_pos, grasp = self.get_gripper_state()
        pre_block_poses, _ = self.get_poses()
        #z_check_collision = self.z_min + 0.02 #0.025

        action_norm = np.array(action) / np.linalg.norm(action)
        gripper_pos = deepcopy(pre_gripper_pos)
        gripper_pos = gripper_pos + action_norm * self.mov_dist
        gripper_pos[0] = np.clip(gripper_pos[0], self.eef_range_x[0], self.eef_range_x[1])
        gripper_pos[1] = np.clip(gripper_pos[1], self.eef_range_y[0], self.eef_range_y[1])

        collision = False
        if self.task < 2:
            im_state = self.env.move_to_pos_slow([*gripper_pos, self.z_push], grasp=grasp)
        else:
            gripper_pos[2] = np.clip(gripper_pos[2], self.z_min, self.z_max)
            if pre_gripper_pos[2] > z_check_collision and gripper_pos[2] < z_check_collision:
                checking_gripper_pos = deepcopy(gripper_pos)
                checking_gripper_pos[2] = z_check_collision
                self.env.move_to_pos_slow(checking_gripper_pos, grasp=grasp)
                # check collision #
                force = self.env.sim.data.sensordata
                if np.abs(force[2]) > 1.0 or np.abs(force[5]) > 1.0:
                    collision = True
                    im_state = self.env.move_to_pos_slow(pre_gripper_pos, grasp=grasp)
                else:
                    im_state = self.env.move_to_pos_slow(gripper_pos, grasp=grasp)
            else:
                im_state = self.env.move_to_pos_slow(gripper_pos, grasp=grasp)

        block_poses, rotations = self.get_poses()

        info = {}
        info['collision'] = collision
        info['out_of_range'] = not self.check_blocks_in_range()
        info['contact'] = np.zeros(self.num_blocks)
        info['goals'] = np.array(self.goals)
        info['pre_poses'] = np.array(pre_block_poses)
        info['poses'] = np.array(block_poses)
        info['rotations'] = np.array(rotations)
        info['goal_flags'] = np.linalg.norm(info['goals']-info['poses'], axis=1) < self.threshold

        reward, done, block_success = self.get_reward(info)
        info['success'] = np.all(block_success)
        info['block_success'] = block_success

        self.step_count += 1
        if self.step_count==self.max_steps:
            done = True

        gripper_pos, grasp = self.get_gripper_state()
        if self.state_type=='feature':
            poses = info['poses'].flatten()
            goals = info['goals'].flatten()
            state = np.concatenate([gripper_pos, poses, goals])
            return state, reward, done, info
        elif self.state_type=='image':
            return im_state, reward, done, info

    def get_poses(self):
        poses = []
        rotations = []
        for obj_idx in range(self.num_blocks):
            pos = deepcopy(self.env.sim.data.get_body_xpos('target_body_%d'%(obj_idx+1))[:2])
            poses.append(pos)
            quat = deepcopy(self.env.sim.data.get_body_xquat('target_body_%d'%(obj_idx+1)))
            rotation_mat = quat2mat(np.concatenate([quat[1:],quat[:1]]))
            rotations.append(rotation_mat[0][:2])
        return poses, rotations

    def check_blocks_in_range(self):
        poses, _ = self.get_poses()
        x_max, y_max = np.concatenate(poses).reshape(-1, 2).max(0)
        x_min, y_min = np.concatenate(poses).reshape(-1, 2).min(0)
        if x_max > self.block_range_x[1] or x_min < self.block_range_x[0]:
            return False
        if y_max > self.block_range_y[1] or y_min < self.block_range_y[0]:
            return False
        return True

    def get_gripper_state(self):
        # get gripper_pose, grasp_close #
        gripper_pos = deepcopy(self.env.sim.data.mocap_pos[0])
        grasp = deepcopy(int(bool(sum(self.env.sim.data.ctrl))))
        if self.task < 2:
            gripper_pos = gripper_pos[:2]
        return gripper_pos, grasp

    def get_reward(self, info):
        # 0: Reach #
        # 1: Push  #
        # 2: Pick  #
        # 3: Place #
        if self.task==0:
            return reward_reach(self)
        elif self.task==1:
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
        else:
            done = False
            reward = 0.0

            reward += -self.time_penalty

            if info['out_of_range']:
                reward = -1.0
                done = True
            elif info['collision']:
                pass
            return reward, done

if __name__=='__main__':
    env = UR5Env(render=True, camera_height=64, camera_width=64, control_freq=5)
    env = continuous_env(env, mov_dist=0.03, max_steps=100, state='image')
    frame = env.reset()
    f, ax = plt.subplots(2)

    for i in range(100):
        #action = [np.random.randint(6), np.random.randint(2)]
        try:
            action = int(input("action? "))
        except KeyboardInterrupt:
            exit()
        except:
            continue
        if action > 10:
            continue
        print('{} steps. action: {}'.format(env.step_count, action))
        states, reward, done, info = env.step(action)

        ax[0].imshow(states[0])
        ax[1].imshow(states[1])
        plt.show()
        print('Reward: {}. Done: {}'.format(reward, done))

        if done:
            print('Done. New episode starts.')
            env.reset()
