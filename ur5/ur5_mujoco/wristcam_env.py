from ur5_env import *

class onesteppush_env(object):
    def __init__(self, ur5_env, num_bins=8, mov_dist=0.05, max_steps=50):
        self.action_type="disc_10d"
        self.env = ur5_env 

        ## env settings ##
        self.init_pos = [0.0, 0.3, 2.0] #[-0.12, 0.0, 1.50]
        self.num_blocks = 3
        self.num_bins = num_bins
        self.mov_dist = mov_dist
        self.z_prepush = 1.12
        self.z_push = 1.08
        self.z_min = 1.05
        self.threshold = 0.02
        self.max_steps = max_steps
        self.time_penalty = 1e-3
        self.colors = np.array([ 
            [0.6784, 1.0, 0.1843], 
            [0.93, 0.545, 0.93], 
            [0.9686, 0.902, 0] 
            ])
        self.range_x_min = 0
        self.range_x_max = 90
        self.range_y_min = 0
        self.range_y_max = 90

        ## camera intrinsic ##
        cam_id = 2
        fovy = self.env.sim.model.cam_fovy[cam_id]
        f = 0.5 * self.env.camera_height / np.tan(fovy*np.pi/360)
        self.K = np.array([[f, 0, self.env.camera_width / 2],
                            [0, f, self.env.camera_height / 2], 
                            [0, 0, 1]])

        ## init env variables ##
        self.success = np.zeros(3)
        self.goal_image = np.zeros([self.env.camera_width, self.env.camera_height])
        self.step_count = 0

        self.set_goal(seed=0)
        self.env.move_to_pos(self.init_pos, 1.0)

        print(self.env.sim.data.get_body_xpos("wrist_3_link"))
        ## camera rotation & translation ##
        self.cam_mat = self.env.sim.data.get_camera_xmat("eye_on_wrist")
        self.cam_pos = self.env.sim.data.get_camera_xpos("eye_on_wrist").reshape([3, 1])
        # self.cam_mat = self.env.sim.model.cam_mat0[cam_id].reshape([3, 3])
        # cam_pos = self.env.sim.model.cam_pos0[cam_id].reshape([3, 1])
        # self.cam_T = np.concatenate([cam_mat, cam_pos], axis=1)
        self.depth = self.cam_pos[2] - 0.9


    def reset(self):
        glfw.destroy_window(self.env.viewer.window)
        self.env.viewer = None
        self.env._init_robot()
        self.step_count = 0

        self.set_goal(seed=0)
        im_state = self.env.move_to_pos(self.init_pos)
        return im_state

    def pixel2pose(self, u, v):
        pos_pixel = np.array([u, v, 1]).transpose()
        pos_cam = np.matmul(np.linalg.inv(self.K), pos_pixel)
        pos_cam = pos_cam / pos_cam[2] * self.depth
        pos_cam = pos_cam.reshape([3, 1])
        pos_world = np.matmul(np.linalg.inv(self.cam_mat), pos_cam) + self.cam_pos
        x, y, z = pos_world
        return x, y, z

    def move_to_pixel(self, px, py, z):
        pos_world = self.pixel2pose(px, py)
        pos_world = [pos_world[0], pos_world[1], self.z_push]
        return self.env.move_to_pos(pos_world, 1.0)

    def get_depth(self, px, py):
        return self.depth

    def push_from_pixel(self, px, py, theta):
        z = self.get_depth(px, py)
        pos_before = np.array(self.pixel2pose(px, py))
        pos_after = pos_before + self.mov_dist * np.array([np.cos(theta), np.sin(theta)])

        self.env.move_to_pos([pos_before[0], pos_before[1], self.z_prepush], 1.0)
        self.env.move_to_pos([pos_before[0], pos_before[1], self.z_push], 1.0)
        self.env.move_to_pos([pos_after[0], pos_after[1], self.z_push], 1.0)
        im_state = self.env.move_to_pos([pos_after[0], pos_after[1], self.z_prepush], 1.0)
        return im_state

    def step(self, action): # action: x, y, theta_idx
        px, py, theta_idx = action
        if theta_idx >= self.num_bins:
            print("Error! theta_idx cannot be bigger than number of angle bins.")
            return
        theta = theta_idx * (2*np.pi / self.num_bins)
        im_state = self.push_from_pixel(px, py, theta)
        reward, done = self.get_reward()

        self.step_count += 1
        if self.step_count == self.max_steps:
            done = True

        return (im_state, self.goal_image), reward, done, None

    def set_goal(self, seed=0):
        np.random.seed(seed)
        goal_positions = []
        for i in range(self.num_blocks):
            goal_x = np.random.randint(self.range_x_min, self.range_x_max)
            goal_y = np.random.randint(self.range_y_min, self.range_y_max)
            goal_positions.append([goal_x, goal_y])

        self.goal_positions = np.array(goal_positions)
        self.goal_image = self.make_goal_image()

    def make_goal_image(self):
        goal_image = np.zeros([self.env.camera_width, self.env.camera_height])
        for i in range(self.goal_positions.shape[0]):
            gx, gy = self.goal_positions[i]
            goal_image = cv2.circle(goal_image, (gx, gy), 3, self.colors[i], 2)
        return goal_image

    def get_reward(self):
        reward = 0.0
        done = False

        block_positions = []
        for i in range(self.num_blocks):
            block_positions.append(self.env.sim.data.get_body_xpos('target_body_%d'%(i+1)))

        ## check one by one ##
        pre_sucess = deepcopy(self.success)
        for i in range(self.num_blocks):
            if np.linalg.norm(block_positions[i] - self.goal_positions[i]) < self.threshold:
                self.success[i] = 1 
            else:
                self.success[i] = 0

        reward = (self.success - pre_success).sum()
        if self.success.sum() == self.num_blocks:
            done = True

        return reward, done



env = UR5Env(render=True, camera_height=96, camera_width=96, camera_name="eye_on_wrist")
env = onesteppush_env(env, num_bins=8, mov_dist=0.05, max_steps=100)
frame = env.reset()

if __name__=='__main__':
    env = UR5Env(render=True, camera_height=96, camera_width=96, control_freq=6, camera_name="eye_on_wrist")
    env = onesteppush_env(env, num_bins=8, mov_dist=0.05, max_steps=100)
    frame = env.reset()
    plt.imshow(frame)
    plt.show()
    print(env.pixel2pose(48, 48))
    print(env.pixel2pose(20, 20))

    for i in range(100):
        #action = [np.random.randint(6), np.random.randint(2)]
        try:
            action = [np.random.randint(100), np.random.randint(100), np.random.randint(8)] #[int(input("action? ")), 1]
        except KeyboardInterrupt:
            exit()
        except:
            continue
        if action[2] > 9:
            continue
        print('{} steps. action: {}'.format(env.step_count, action))
        states, reward, done, info = env.step(action)
        print('Reward: {}. Done: {}'.format(reward, done))
        #show_image(states[0])
        if done:
            print('Done. New episode starts.')
            env.reset()
