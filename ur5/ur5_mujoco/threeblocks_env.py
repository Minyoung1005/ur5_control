from ur5_env import *
import cv2


class discrete_env(object):
    def __init__(self, ur5_env, task=1, mov_dist=0.03, max_steps=50):
        self.action_type="disc_10d"
        self.env = ur5_env 
        self.init_pos = [0.0, 0.0, 1.20]
        self.task = task
        if self.task==0:
            self.init_pos = [0.0, 0.0, 1.20]
        elif self.task==1:
            self.threshold = 0.4
        elif self.task==2:
            self.threshold = 0.1
        elif self.task==3:
            self.threshold = np.pi/18
        else:
            pass
        self.mov_dist = mov_dist
        self.z_min = 1.05
        self.time_penalty = 1e-3
        self.max_steps = max_steps
        self.step_count = 0

        self.cam_id = 1
        self.cam_theta = 30 * np.pi / 180
        # cam_mat = self.env.sim.data.get_camera_xmat("rlview")
        # cam_pos = self.env.sim.data.get_camera_xpos("rlview")
        self.env.sim.data.qpos[12:15] = [0, 0, 0.9]
        self.env.sim.data.qpos[19:22] = [0, 0, 0]
        self.env.sim.data.qpos[26:29] = [0, 0, 0]

        self.env.move_to_pos(self.init_pos, grasp=1.0)

    def reset(self):
        glfw.destroy_window(self.env.viewer.window)
        self.env.viewer = None
        self.env._init_robot()
        gripper_height, curr_grasp = self.get_gripper_state()
        self.env.sim.data.qpos[12:15] = [0, 0, 0.9]
        self.env.sim.data.qpos[19:22] = [0, 0, 0]
        self.env.sim.data.qpos[26:29] = [0, 0, 0]
        im_state = self.env.move_to_pos(self.init_pos)
        self.step_count = 0
        return im_state, np.array([gripper_height, curr_grasp])

    def step(self, action, grasp):
        self.pre_mocap_pos = deepcopy(self.env.sim.data.mocap_pos[0])
        self.pre_target_pos = deepcopy(self.env.sim.data.get_body_xpos('target_body_1'))

        dist = self.mov_dist
        if self.action_type=="disc_6d":
            if action==0:
                im_state = self.env.move_pos_diff([0.0, dist, 0.0], grasp=grasp)
            elif action==1:
                im_state = self.env.move_pos_diff([dist, 0.0, 0.0], grasp=grasp)
            elif action==2:
                im_state = self.env.move_pos_diff([0.0, -dist, 0.0], grasp=grasp)
            elif action==3:
                im_state = self.env.move_pos_diff([-dist, 0.0, 0.0], grasp=grasp)
            elif action==4:
                im_state = self.env.move_pos_diff([0.0, 0.0, dist], grasp=grasp)
            elif action==5:
                if self.pre_mocap_pos[2]-dist < self.z_min:
                    im_state = self.env.move_pos_diff([0.0, 0.0, -self.pre_mocap_pos[2]+self.z_min], grasp=grasp)
                else:
                    im_state = self.env.move_pos_diff([0.0, 0.0, -dist], grasp=grasp)
            else:
                print("Error!! Wrong action!")
        elif self.action_type=="disc_10d":
            dist2 = dist/np.sqrt(2)
            if action==0:
                if self.pre_mocap_pos[2]-dist < self.z_min:
                    im_state = self.env.move_pos_diff([0.0, 0.0, -self.pre_mocap_pos[2]+self.z_min], grasp=grasp)
                else:
                    im_state = self.env.move_pos_diff([0.0, 0.0, -dist], grasp=grasp)
            elif action==5:
                im_state = self.env.move_pos_diff([0.0, 0.0, dist], grasp=grasp)
            elif action==8:
                im_state = self.env.move_pos_diff([0.0, dist, 0.0], grasp=grasp)
            elif action==9:
                im_state = self.env.move_pos_diff([dist2, dist2, 0.0], grasp=grasp)
            elif action==6:
                im_state = self.env.move_pos_diff([dist, 0.0, 0.0], grasp=grasp)
            elif action==3:
                im_state = self.env.move_pos_diff([dist2, -dist2, 0.0], grasp=grasp)
            elif action==2:
                im_state = self.env.move_pos_diff([0.0, -dist, 0.0], grasp=grasp)
            elif action==1:
                im_state = self.env.move_pos_diff([-dist2, -dist2, 0.0], grasp=grasp)
            elif action==4:
                im_state = self.env.move_pos_diff([-dist, 0.0, 0.0], grasp=grasp)
            elif action==7:
                im_state = self.env.move_pos_diff([-dist2, dist2, 0.0], grasp=grasp)
            else:
                print("Error!! Wrong action!")

        gripper_height, curr_grasp = self.get_gripper_state()
        reward, done = self.get_reward()

        self.step_count += 1
        if self.step_count==self.max_steps:
            done = True

        sim = self.env.sim
        # left_finger_idx = sim.model.body_name2id('left_inner_finger')
        # right_finger_idx = sim.model.body_name2id('right_inner_finger')
        # right_contact_force = sim.data.efc_force[right_finger_idx]
        # # print('left: {} / right: {}'.format(left_contact_force, right_contact_force))
        print('force: {}'.format(sim.data.sensordata))
        # print(sim.data.get_sensor('left_finger_force'))

        return [im_state, np.array([gripper_height, curr_grasp])], reward, done, None

    def get_gripper_state(self):
        # return grasp_height, gripper_close
        return self.env.sim.data.mocap_pos[0][2], int(bool(sum(self.env.sim.data.ctrl)))

    def get_reward(self):
        # 0: Reach   #
        # 1: Spread  #
        # 2: Gather  #
        # 3: Line up #
        ## Reach ##
        if self.task == 0:
            target_pos = self.env.sim.data.get_body_xpos('target_body_1')
            if np.linalg.norm(target_pos - self.pre_target_pos) > 1e-3:
                reward = 1.0
                done = True
            else:
                reward = -self.time_penalty
                done = False
        ## Spread ##
        elif self.task == 1:
            pos_1 = self.env.sim.data.get_body_xpos('target_body_1')
            pos_2 = self.env.sim.data.get_body_xpos('target_body_2')
            pos_3 = self.env.sim.data.get_body_xpos('target_body_3')
            dist_12 = np.linalg.norm(pos_1 - pos_2)
            dist_23 = np.linalg.norm(pos_2 - pos_3)
            dist_31 = np.linalg.norm(pos_3 - pos_1)
            min_dist = np.min([dist_12, dist_23, dist_31])
            if min_dist > self.threshold:
                reward = 1.0
                done = True
            else:
                reward = 0.0
                done = False
        ## Gather ##
        elif self.task == 2:
            pos_1 = self.env.sim.data.get_body_xpos('target_body_1')
            pos_2 = self.env.sim.data.get_body_xpos('target_body_2')
            pos_3 = self.env.sim.data.get_body_xpos('target_body_3')
            dist_12 = np.linalg.norm(pos_1 - pos_2)
            dist_23 = np.linalg.norm(pos_2 - pos_3)
            dist_31 = np.linalg.norm(pos_3 - pos_1)
            max_dist = np.max([dist_12, dist_23, dist_31])
            if max_dist < self.threshold:
                reward = 1.0
                done = True
            else:
                reward = 0.0
                done = False
        ## Line Up ##
        elif self.task==3:
            pos_1 = self.env.sim.data.get_body_xpos('target_body_1')
            pos_2 = self.env.sim.data.get_body_xpos('target_body_2')
            pos_3 = self.env.sim.data.get_body_xpos('target_body_3')
            theta_12 = np.arctan((pos_1[1] - pos_2[1])/(pos_1[0] - pos_2[0] + 1e-10))
            theta_23 = np.arctan((pos_2[1] - pos_3[1])/(pos_2[0] - pos_3[0] + 1e-10))
            theta_31 = np.arctan((pos_3[1] - pos_1[1])/(pos_3[0] - pos_1[0] + 1e-10))
            dtheta_1 = np.min([(theta_12-theta_31)%np.pi, np.abs((theta_12-theta_31)%np.pi-np.pi)])
            dtheta_2 = np.min([(theta_12-theta_23)%np.pi, np.abs((theta_12-theta_23)%np.pi-np.pi)])
            dtheta_3 = np.min([(theta_31-theta_23)%np.pi, np.abs((theta_31-theta_23)%np.pi-np.pi)])
            max_dtheta = np.max([dtheta_1, dtheta_2, dtheta_3])
            if max_dtheta < self.threshold:
                reward = 1.0
                done = True
            else:
                reward = 0.0
                done = False
        else:
            reward = 0.0
            done = False
        return reward, done

    def pixel2pos(self, u, v):
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
        return u, v

    def move2pixel(self, u, v):
        target_pos = np.array(self.pixel2pos(u, v))
        target_pos[2] = 1.05
        frame = self.env.move_to_pos(target_pos)
        plt.imshow(frame)
        plt.show()

if __name__=='__main__':
    env = UR5Env(render=True, camera_height=96, camera_width=96, control_freq=5)
    env = discrete_env(env, task=3, mov_dist=0.03, max_steps=100)
    frame = env.reset()
    img = cv2.circle(frame[0].astype(np.float32), (10, 50), 1, [255, 0, 0], 1)
    plt.imshow(img/255)
    plt.show()

    env.move2pixel(48, 48)
    env.move2pixel(48, 60)
    env.move2pixel(48, 70)
    env.move2pixel(20, 48)
    env.move2pixel(20, 20)
    env.move2pixel(0, 20)

    for i in range(100):
        #action = [np.random.randint(6), np.random.randint(2)]
        try:
            action = [int(input("action? ")), 1]
        except KeyboardInterrupt:
            exit()
        except:
            continue
        if action[0] > 9:
            continue
        print('{} steps. action: {}'.format(env.step_count, action))
        states, reward, done, info = env.step(*action)
        print('Reward: {}. Done: {}'.format(reward, done))
        #show_image(states[0])
        if done:
            print('Done. New episode starts.')
            env.reset()
