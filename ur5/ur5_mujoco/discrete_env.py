import cv2
from ur5_env import *
from transform_utils import euler2quat, quat2mat

class discrete_env(object):
    def __init__(self, ur5_env, mov_dist=0.03, max_steps=50, task=1, state='feature', reward_type='new'):
        self.env = ur5_env
        self.task = task # 0: Reach / 1: Push / 2: Pick / 3: Place
        if self.task==0:
            self.action_range = 10
        elif self.task==1:
            self.action_range = 8
        else:
            self.action_range = 11

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
        self.time_penalty = 1e-2
        self.max_steps = max_steps
        self.step_count = 0
        self.threshold = 0.05

        self.init_pos = [0.0, 0.0, self.z_min + self.mov_dist]
        self.init_env()

    def init_env(self):
        self.env._init_robot()
        range_x = self.block_spawn_range_x
        range_y = self.block_spawn_range_y
        self.env.sim.data.qpos[12:15] = [0, 0, 0]
        self.env.sim.data.qpos[19:22] = [0, 0, 0]
        self.env.sim.data.qpos[26:29] = [0, 0, 0]
        for obj_idx in range(2):
            tx = np.random.uniform(*range_x)
            ty = np.random.uniform(*range_y)
            tz = 0.9
            self.env.sim.data.qpos[7 * obj_idx + 12: 7 * obj_idx + 15] = [tx, ty, tz]

        im_state = self.env.move_to_pos(self.init_pos, grasp=1.0)
        self.step_count = 0

        return im_state

    def reset(self):
        im_state = self.init_env()
        gripper_height = self.get_gripper_state()
        if self.task==0:
            return im_state, gripper_height
        else:
            return im_state, self.goal_image, gripper_height

    def step(self, action):
        assert action < self.action_range
        pre_gripper_pos, grasp = self.get_gripper_state()
        pre_block_poses, _ = self.get_poses()
        z_check_collision = self.z_min + 0.02 #0.025

        collision = False
        dist = self.mov_dist
        dist2 = dist/np.sqrt(2)
        if action==8:
            if pre_gripper_pos[2] - dist < self.z_min:
                gripper_pos = deepcopy(pre_gripper_pos)
                gripper_pos[2] = self.z_min
                im_state = self.env.move_to_pos(gripper_pos, grasp=grasp)
            else:
                if pre_gripper_pos[2] - dist < z_check_collision:
                    gripper_pos = deepcopy(pre_gripper_pos)
                    gripper_pos[2] = z_check_collision
                    self.env.move_to_pos(gripper_pos, grasp=grasp)
                    # check collision #
                    force = self.env.sim.data.sensordata
                    if np.abs(force[2]) > 1.0 or np.abs(force[5]) > 1.0:
                        collision = True
                        im_state = self.env.move_to_pos(pre_gripper_pos, grasp=grasp)
                    else:
                        gripper_pos[2] = pre_gripper_pos[2] - dist
                        im_state = self.env.move_to_pos(gripper_pos, grasp=grasp)
                else:
                    im_state = self.env.move_pos_diff([0.0, 0.0, -dist], grasp=grasp)

        elif action==9:
            if pre_gripper_pos[2]+dist > self.z_max:
                im_state = self.env.move_pos_diff([0.0, 0.0, -pre_mocap_pos[2]+self.z_max], grasp=grasp)
            else:
                im_state = self.env.move_pos_diff([0.0, 0.0, dist], grasp=grasp)

        else:
            gripper_pos = deepcopy(pre_gripper_pos)
            if action==0:
                gripper_pos[1] = np.min([gripper_pos[1] + dist, self.eef_range_y[1]])
                #im_state = self.env.move_pos_diff([0.0, dist, 0.0], grasp=grasp)
            elif action==1:
                gripper_pos[0] = np.min([gripper_pos[0] + dist2, self.eef_range_x[1]])
                gripper_pos[1] = np.min([gripper_pos[1] + dist2, self.eef_range_y[1]])
                #im_state = self.env.move_pos_diff([dist2, dist2, 0.0], grasp=grasp)
            elif action==2:
                gripper_pos[0] = np.min([gripper_pos[0] + dist, self.eef_range_x[1]])
                #im_state = self.env.move_pos_diff([dist, 0.0, 0.0], grasp=grasp)
            elif action==3:
                gripper_pos[0] = np.min([gripper_pos[0] + dist2, self.eef_range_x[1]])
                gripper_pos[1] = np.max([gripper_pos[1] - dist2, self.eef_range_y[0]])
                #im_state = self.env.move_pos_diff([dist2, -dist2, 0.0], grasp=grasp)
            elif action==4:
                gripper_pos[1] = np.max([gripper_pos[1] - dist, self.eef_range_y[0]])
                #im_state = self.env.move_pos_diff([0.0, -dist, 0.0], grasp=grasp)
            elif action==5:
                gripper_pos[0] = np.max([gripper_pos[0] - dist2, self.eef_range_x[0]])
                gripper_pos[1] = np.max([gripper_pos[1] - dist2, self.eef_range_y[0]])
                #im_state = self.env.move_pos_diff([-dist2, -dist2, 0.0], grasp=grasp)
            elif action==6:
                gripper_pos[0] = np.max([gripper_pos[0] - dist, self.eef_range_x[0]])
                #im_state = self.env.move_pos_diff([-dist, 0.0, 0.0], grasp=grasp)
            elif action==7:
                gripper_pos[0] = np.max([gripper_pos[0] - dist2, self.eef_range_x[0]])
                gripper_pos[1] = np.min([gripper_pos[1] + dist2, self.eef_range_y[1]])
                #im_state = self.env.move_pos_diff([-dist2, dist2, 0.0], grasp=grasp)
            elif action==10:
                grasp = 1. - grasp
            im_state = self.env.move_to_pos(gripper_pos, grasp=grasp)

        info = {}
        info['collision'] = collision
        info['out_of_range'] = not self.check_blocks_in_range()
        info['goals'] = np.array(self.goals)
        info['pre_poses'] = np.array(pre_poses)
        info['poses'] = np.array(poses)
        info['rotations'] = np.array(rotations)
        info['goal_flags'] = np.linalg.norm(info['goals']-info['poses'], axis=1) < self.threshold

        reward, success, block_success = self.get_reward(info)
        info['success'] = success
        info['block_success'] = block_success

        self.step_count += 1
        done = success
        if self.step_count==self.max_steps:
            done = True

        gripper_pose, grasp = self.get_gripper_state()
        if self.state_type=='feature':
            poses = info['poses'].flatten()
            goals = info['goals'].flatten()
            state = np.concatenate([gripper_pose, poses, goals])
            return state, reward, done, info
        elif self.state_type=='image':
            return im_state, reward, done, info

    def get_poses(self):
        poses = []
        rotations = []
        for obj_idx in range(2):
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
        return deepcopy(self.env.sim.data.mocap_pos[0]), deepcopy(int(bool(sum(self.env.sim.data.ctrl))))

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
    env = discrete_env(env, mov_dist=0.03, max_steps=100, state='image')
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
