import os
from utils_ur5 import *
from transform_utils import *
from PIL import Image

class UR5Robot(object):
    X_MIN = -0.5
    X_MAX = 0.5
    Y_MIN = -0.85
    Y_MAX = -0.2 #-0.3
    Z_MIN = 0.18
    Z_MAX = 0.8

    X_WS_MIN = -0.4 #-0.3
    X_WS_MAX = 0.4 #0.3
    Y_WS_MIN = -0.8 #-0.75
    Y_WS_MAX = -0.25 #-0.35
    Z_WS_MIN = 0.19
    Z_WS_MAX = 0.25
    # new frame init pose: [-0.0281, -0.2988, 0.6489]
    # new frame init quat: [0.9990, -0.0441, -0.0026, -0.0029]
    #ROBOT_INIT_POS = [-0.0468, -0.4978, 0.6489]
    #ROBOT_INIT_QUAT = [0.9990, -0.0441, -0.0026, -0.0029]
    ROBOT_INIT_POS = [0, -0.47, 0.65]
    ROBOT_INIT_QUAT = [1, 0, 0, 0]
    #ROBOT_INIT_POS = [0, -0.15, 0.65] #[0, -0.5, 0.65]
    #ROBOT_INIT_QUAT = [0.9808, 0.0, 0.0, 0.1951] #[1, 0, 0, 0]

    ARM_JOINT_NAME = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
    ROBOT_INIT_ROTATION = quat2mat(ROBOT_INIT_QUAT)
    #ROBOT_INIT_ROTATION = np.array([[1., 0., 0.], [0., -1., 0.], [0., 0., -1.]])

    def __init__(self, cam_id="141322252613"):
        self.mov_dist = 0.07 #0.08
        self.z_prepush = 0.25 #0.25
        self.z_push = 0.18 #0.2

        self.cam_id = cam_id
        self.realsense = None
        self.set_realsense()

        self.planUR5 = None
        self.moveUR5 = None
        self.getEEFPose = None
        self.getJointStates = None
        self.get_ur5_control_service()

        self.T_eef_to_rs = np.load('rs_extrinsic.npy')
        #self.T_eef_to_rs = np.load('rs_extrinsic_secondUR5.npy')

        self.twist = True
        self.twist_quat = [-0.0027, -0.0027, -0.0441, 0.999] # xyzw
        self.twist_rotation = quat2mat(self.twist_quat)
        self.twist_inverse_rotation = quat2mat(quat_inverse(self.twist_quat))

    def set_realsense(self):
        self.realsense = RealSenseSensor(self.cam_id)
        self.K_rs = self.realsense._color_intrinsics
        self.D_rs = 0
        return

    def get_ur5_control_service(self):
        self.planUR5 = rospy.ServiceProxy('plan_robot_arm', JointTrajectory)
        rospy.wait_for_service('plan_robot_arm')
        self.moveUR5 = rospy.ServiceProxy('move_robot_arm', JointTrajectory)
        rospy.wait_for_service('move_robot_arm')
        self.getEEFPose = rospy.ServiceProxy('get_eef_pose', EndPose)
        rospy.wait_for_service('get_eef_pose')
        self.getJointStates = rospy.ServiceProxy('get_joint_states', JointStates)
        rospy.wait_for_service('get_joint_states')
        return 

    def get_joint_states(self):
        joints_Str = self.getJointStates().joint_states.replace('(', '').replace(')', '').split(', ')
        joints = [float(j) for j in joints_Str]
        return joints

    def get_eef_pose(self):
        pose = self.getEEFPose().eef_pose
        position = [pose.position.x, pose.position.y, pose.position.z]
        quaternion = [pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w]
        if self.twist:
            T_robot_to_goal = form_T(quat2mat(quaternion), pose)
            T_base_to_robot = form_T(self.twist_inverse_rotation, [0, 0, 0])
            T_base_to_goal = T_base_to_robot.dot(T_robot_to_goal)
            position = T_base_to_goal[:3, 3]
            quaterion = mat2quat(T_base_to_goal[:3, :3])
        return position, quaternion

    def reset_wrist3(self):
        qpos = self.get_joint_states()
        qpos[5] = qpos[5]%(2*np.pi)
        if qpos[5] > np.pi:
            qpos[5] -= 2*np.pi
        self.moveUR5(self.ARM_JOINT_NAME, qpos, None, None, 1.0)

    def move_to_pose(self, goal_pos, quat=[1,0,0,0], grasp=0.0):
        if self.twist:
            T_base_to_goal = form_T(quat2mat(quat), goal_pos)
            T_robot_to_base = form_T(self.twist_rotation, [0, 0, 0])
            T_robot_to_goal = T_robot_to_base.dot(T_base_to_goal)
            goal_pos = T_robot_to_goal[:3, 3]
            quat = mat2quat(T_robot_to_goal[:3, :3])
        plans = self.moveUR5(self.ARM_JOINT_NAME, None, goal_pos, quat, 1-grasp)
        return plans

    def get_view(self, goal_pos=None, quat=[1, 0, 0, 0], grasp=0.0, show_img=False):
        # quat: xyzw
        if goal_pos is not None:
            plans = self.move_to_pose(goal_pos, quat, grasp)
            if len(plans.plan.points)<=1:
                print("Failed planning to the goal.")
                return None, None
        rospy.sleep(1.0)
        color, depth = self.realsense.frames(spatial=True, hole_filling=True, temporal=True)
        if show_img:
            plt.imshow(color)
            plt.show()
        return color, depth

    def get_view_at_ws_init(self):
        self.move_to_pose(self.ROBOT_INIT_POS, quat=self.ROBOT_INIT_QUAT, grasp=0.0)
        rospy.sleep(0.5)
        self.reset_wrist3()
        color, depth = self.realsense.frames(spatial=True, hole_filling=True, temporal=True)
        return color, depth

    def pixel2pos(self, depth, goal_pixel):
        goal_pixel = np.array(goal_pixel)
        p_rs_to_goal = inverse_projection(depth, goal_pixel, self.K_rs, self.D_rs)
        #print(p_rs_to_goal)
        
        T_base_to_initeef = form_T(self.ROBOT_INIT_ROTATION, self.ROBOT_INIT_POS)
        T_rs_to_goal = form_T(np.eye(3), p_rs_to_goal)

        T_base_to_goal = T_base_to_initeef.dot(self.T_eef_to_rs.dot(T_rs_to_goal))    
        goal_position = T_base_to_goal[:3, 3]
        return goal_position

    def clip_pose(self, pose):
        pose[0] = np.clip(pose[0], self.X_MIN, self.X_MAX)
        pose[1] = np.clip(pose[1], self.Y_MIN, self.Y_MAX)
        pose[2] = np.clip(pose[2], self.Z_MIN, self.Z_MAX)
        return pose

    def clip_ws_pose(self, pose):
        pose[0] = np.clip(pose[0], self.X_WS_MIN, self.X_WS_MAX)
        pose[1] = np.clip(pose[1], self.Y_WS_MIN, self.Y_WS_MAX)
        pose[2] = np.clip(pose[2], self.Z_WS_MIN, self.Z_WS_MAX)
        return pose

    def push_from_pixel(self, depth, px, py, theta):
        if depth is None:
            color, depth = self.get_view_at_ws_init()
            #color, depth = self.get_view(self.ROBOT_INIT_POS, grasp=1.0)
            return color, depth
        pos_before = np.array(self.pixel2pos(depth, [px, py]))
        pos_before = self.clip_ws_pose(pos_before)
        pos_after = pos_before + self.mov_dist * np.array([-np.sin(theta), -np.cos(theta), 0.])
        pos_after = self.clip_ws_pose(pos_after)

        # gripper rotation #
        theta_gp = (theta + np.pi/2) % np.pi - np.pi/2
        x, y, z, w = euler2quat([-theta_gp, 0., 0.]) # +np.pi/2
        quat = [w, x, y, z]
        self.move_to_pose(self.ROBOT_INIT_POS, quat, grasp=1.0)
        x_bias = -0.01
        y_bias = 0.0 #-0.01
        for i in range(1):
            plans = self.move_to_pose([pos_before[0] + x_bias, pos_before[1] + y_bias, self.z_prepush], quat, grasp=1.0)
            if len(plans.plan.points)<=1:
                print("Failed planning to the Pre-push Pose.")
                break
            else:
                print("Plan to the Pre-push Pose:", len(plans.plan.points))
            plans = self.move_to_pose([pos_before[0] + x_bias, pos_before[1] + y_bias, self.z_push], quat, grasp=1.0)
            if len(plans.plan.points)<=1:
                print("Failed planning to the Push Starting Pose.")
                break
            else:
                print("Plan to the Starting Pose:", len(plans.plan.points))
            plans = self.move_to_pose([pos_after[0] + x_bias, pos_after[1] + y_bias, self.z_push], quat, grasp=1.0)
            if len(plans.plan.points)<=1:
                print("Failed planning to the Push Ending Pose.")
                break
            else:
                print("Plan to the Ending Pose:", len(plans.plan.points))
            self.move_to_pose([pos_after[0] + x_bias, pos_after[1] + y_bias, self.z_prepush], quat, grasp=1.0)
        rospy.sleep(0.5)
        color, depth = self.get_view_at_ws_init()
        #color, depth = self.get_view(self.ROBOT_INIT_POS, grasp=1.0)
        return color, depth
        
    
class RealUR5Env(object):
    def __init__(self, ur5robot, seg_module, num_blocks=3, goal_type='pixel'):
        self.goal_type = goal_type
        self.num_blocks = num_blocks
        self.seg_target = None
        self.max_steps = 50 #30
        self.num_bins = 8


        self.ur5 = ur5robot
        self.seg_module = seg_module
        self.target = None
        self.target_color = None
        self.goal_scene = None
        self.goals = None
        self.goal_centers = None
        self.goal_colors = None

        self.timestep = 0
        self.color = None
        self.depth = None

    def set_target_with_color(self, color):
        # color: [R, G, B]
        target_obj= np.argmin(np.linalg.norm(self.goal_colors - color, axis=1))
        self.set_target(target_obj)

    def set_target(self, target):
        self.seg_target = target

    def reset(self):
        color, depth = self.ur5.get_view_at_ws_init()
        #color, depth = self.ur5.get_view(self.ur5.ROBOT_INIT_POS, grasp=1.0)
        self.target = None
        self.target_color = None
        self.timestep = 0

        color, depth = self.ur5.push_from_pixel(None, 0, 0, 0)
        self.real_depth = depth
        color, depth = self.crop_resize(color, depth)
        return [[color, depth], self.goals]

    def crop_resize(self, color, depth):
        midx, midy = self.ur5.K_rs[:2, 2]
        # crop and resize
        color = resize_image(crop_image(color, midx, midy, 480), 96, 96)
        depth = resize_image(crop_image(depth, midx, midy, 480), 96, 96)
        return color, depth
    
    def crop_resize_pad(self, color, depth):
        midx, midy = self.ur5.K_rs[:2, 2]
        # crop and resize
        color = resize_image(crop_image(color, midx, midy, 480), 80, 80)
        depth = resize_image(crop_image(depth, midx, midy, 480), 80, 80)
        color = np.pad(color, [[8, 8], [8, 8], [0, 0]], mode='edge')
        depth = np.pad(depth, [[8, 8], [8, 8]], mode='edge')
        return color, depth

    def set_goals(self):
        color, depth = self.ur5.get_view_at_ws_init()
        #color, depth = self.ur5.get_view(self.ur5.ROBOT_INIT_POS, grasp=1.0)
        goal_color, goal_depth = self.ur5.get_view(grasp=1.0)
        goal_color, goal_depth = self.crop_resize(goal_color, goal_depth)
        self.goal_scene = [goal_color, goal_depth]
        if self.goal_type=='block':
            self.goals = [goal_color, goal_depth]

        elif self.goal_type=='pixel':
            masks, colors, fmask = self.seg_module.get_masks(
                    goal_color, goal_depth, n_cluster=self.num_blocks)
            goal_ims = []
            goal_centers = []
            for _mask in masks:
                zero_array = np.zeros([96, 96])
                _x, _y = np.where(_mask)
                mx = int(np.round(_x.mean()))
                my = int(np.round(_y.mean()))
                cv2.circle(zero_array, (mx, my), 1, 1, -1)
                goal_ims.append(zero_array)
                goal_centers.append([mx, my])
            self.goals = goal_ims
            self.goal_centers = np.array(goal_centers)
            self.goal_colors = colors
        return

    # for seg_fcdqn
    def step(self, action, mapping=True):
        px, py, theta_idx = action
        theta = theta_idx * (2*np.pi / 8)

        midx, midy = self.ur5.K_rs[:2, 2]
        if mapping:
            PX, PY = inverse_raw_pixel(np.array([px, py]), midx, midy, cs=480, ih=96, iw=96)
        else:
            PX, PY = px, py
        color, depth = self.ur5.push_from_pixel(self.real_depth, PX, PY, theta)
        self.real_depth = depth
        color, depth = self.crop_resize(color, depth)

        reward = 0.0
        done = False
        info = None
        return [[color, depth], self.goals], reward, done, info


class RealSDFEnv(object):
    def __init__(self, ur5robot, sdf_module, num_blocks=3):
        self.max_steps = 50 #30
        self.num_bins = 8

        self.ur5 = ur5robot
        self.midx, self.midy = 424, 240
        #self.midx, self.midy = self.ur5.K_rs[:2, 2].round().astype(int) # 424, 240
        self.sdf_module = sdf_module
        self.num_blocks = num_blocks
        self.goals = None
        self.goal_centers = None
        self.goal_colors = None

        self.timestep = 0
        self.color = None
        self.depth = None
        self.consider_tilt = False

    def reset(self):
        self.timestep = 0
        color_raw, depth_raw = self.ur5.get_view_at_ws_init()
        #color_raw, depth_raw = self.ur5.push_from_pixel(None, 0, 0, 0)
        self.real_depth = depth_raw
        color, depth = self.crop_resize(color_raw, depth_raw)
        color = color/255.
        return [[color, depth], self.goals]

    def crop_resize(self, color, depth):
        # crop only #
        color = crop_image(color, self.midx, self.midy, 480)
        depth = crop_image(depth, self.midx, self.midy, 480)
        # crop and resize #
        # color = resize_image(crop_image(color, self.midx, self.midy, 480), 96, 96)
        # depth = resize_image(crop_image(depth, self.midx, self.midy, 480), 96, 96)
        return color, depth

    def save_init(self, color):
        ni = len([f for f in os.listdir('scenarios/') if 'init_' in f and '.png' in f])
        ng = len([f for f in os.listdir('scenarios/') if 'goal_' in f and '.png' in f])
        if ni!=ng:
            im = Image.fromarray((color * 255).astype(np.uint8))
            im.save('scenarios/init_%02d.png'%ni)
        return

    def save_goals(self):
        goal_color, goal_depth = self.goals
        ng = len([f for f in os.listdir('scenarios/') if 'goal_' in f and '.png' in f])
        np.save('scenarios/rgb_goal_%02d.npy'%ng, goal_color)
        np.save('scenarios/depth_goal_%02d.npy'%ng, goal_depth)
        im = Image.fromarray((goal_color * 255).astype(np.uint8))
        im.save('scenarios/goal_%02d.png'%ng)
        return
    
    def load_goals(self, goal_scene):
        goal_color = np.load('scenarios/rgb_goal_%s.npy'%goal_scene)
        goal_depth = np.load('scenarios/depth_goal_%s.npy'%goal_scene)
        self.goals = [goal_color, goal_depth]
        return

    def set_goals(self):
        color, depth = self.ur5.get_view_at_ws_init()
        #color, depth = self.ur5.get_view(self.ur5.ROBOT_INIT_POS, grasp=1.0)
        goal_color, goal_depth = self.ur5.get_view(grasp=1.0)
        goal_color, goal_depth = self.crop_resize(goal_color, goal_depth)
        goal_color = goal_color/255.
        self.goals = [goal_color, goal_depth]
        return

    def scaling_pixel(self, px, py, src=80, dest=96, offset=8):
        x = np.round((px - 8) * dest / src).astype(int)
        y = np.round((py - 8) * dest / src).astype(int)
        return x, y

    def remap_action(self, px, py, theta):
        return px, py, (theta+4)%8

    # object-wise action
    def step(self, action, sdfs, sdfs_g=None, depth=None, masks=None):
        # sdfs: list of SDFs of objects in current scene #
        # self.depth: depth image in resized resolution  #
        # self.real_depth: depth image in original resol #
        # PX, PY: pushing pixel in original resolution   #
        # rx_before, ry_before: real world position      #
        obj, theta = action
        sdf = sdfs[obj]
        sdfs_mask = masks.sum(0)
        #sdfs_mask = (sdfs>0).sum(0)
        py, px = np.where(sdf>=0)
        py = np.round(np.mean(py)).astype(int)
        px = np.round(np.mean(px)).astype(int)
        #py, px = np.where(sdf==sdf.max())   # center pixel of SDF #
        #px = px[0]
        #py = py[0]

        if self.consider_tilt:
            cam_theta = np.pi / 8
            PX, PY = inverse_raw_pixel(np.array([px, py]), self.midx, self.midy, \
                                    cs=480, ih=96, iw=96)
            rx, ry = np.array(self.ur5.pixel2pos(self.real_depth, (PX, PY)))[:2]
            delta_depth = self.sdf_module.depth_bg - depth
            #delta_depth = cv2.resize(delta_depth, (96, 96), interpolation=cv2.INTER_AREA)
            delta_depth = cv2.resize(delta_depth, (80, 80), interpolation=cv2.INTER_AREA)
            delta_depth = np.pad(delta_depth, [[8, 8], [8, 8]], mode='edge')
            dy = delta_depth[sdf>0].max() * np.sin(cam_theta) / 2
            for i in range(1, 40):
                PX, PY = inverse_raw_pixel(np.array([px, py+i]), self.midx, self.midy, \
                                        cs=480, ih=96, iw=96)
                rx2, ry2 = np.array(self.ur5.pixel2pos(self.real_depth, (PX, PY)))[:2]
                if ry2 - ry > dy:
                    py = py + i
                    break

        # Remap Action to Realworld Frame #
        px, py, theta = self.remap_action(px, py, theta)
        theta = theta * np.pi / 4.

        # Find Starting Point of Pushing #
        vec = np.round(np.sqrt(2) * np.array([-np.sin(theta), np.cos(theta)])).astype(int)
        count_negative = 0
        px_before, py_before = px, py                      # starting pixel in resized resol #
        px_before2, py_before2 = px + vec[0], py + vec[1]  # for collision checking #
        while count_negative < 3:
            px_before += vec[0]
            py_before += vec[1]
            px_before2 += vec[0]
            py_before2 += vec[1]
            if px_before <0 or py_before < 0:
                px_before -= vec[0]
                py_before -= vec[1]
                break
            elif px_before >= sdf.shape[0] or py_before >= sdf.shape[1]:
                px_before -= vec[0]
                py_before -= vec[1]
                break
            if sdfs_mask[py_before, px_before] <= 0 and sdfs_mask[py_before2, px_before2] <= 0:
                count_negative += 1

            PX, PY = inverse_raw_pixel(np.array([px_before, py_before]), self.midx, self.midy, \
                                    cs=480, ih=96, iw=96)   # pixel in original resol #
            rx_before, ry_before = np.array(self.ur5.pixel2pos(self.real_depth, (PX, PY)))[:2]
            '''
            if rx_before < self.ur5.X_MIN or rx_before > self.ur5.X_MAX:
                break
            elif ry_before < self.ur5.Y_MIN or ry_before > self.ur5.Y_MAX:
                break
            '''

        PX, PY = inverse_raw_pixel(np.array([px_before, py_before]), self.midx, self.midy, cs=480, ih=96, iw=96)

        color_raw, depth_raw = self.ur5.push_from_pixel(self.real_depth, PX, PY, theta)
        self.real_depth = depth_raw
        color, depth = self.crop_resize(color_raw, depth_raw)
        color = color/255.

        reward = 0.0
        info = None

        done = False
        #if sdfs_g is not None:
        #    nblock = max(len(sdfs), len(sdfs_g))
        #    sdf_success = self.sdf_module.check_sdf_align(sdfs, sdfs_g, nblock)
        #    done = np.all(sdf_success)
        #    if done:
        #        print("Success!! All SDFs are aligned!")

        self.timestep += 1
        if self.timestep==self.max_steps:
            done = True
        return [[color, depth], self.goals], reward, done, info

    def get_center_from_sdf(self, sdf, depth):
        px, py = np.where(sdf>=0)
        px = np.round(np.mean(px)).astype(int)
        py = np.round(np.mean(py)).astype(int)
        #px, py = np.where(sdf==sdf.max())
        #px = px[0]
        #py = py[0]
        cx, cy, _ = self.ur5.pixel2pos(depth, (px, py))
        #dy = (self.depth_bg - depth)[sdf>0].max() * np.sin(self.cam_theta) / 2
        #cy += dy
        return cx, cy


class RealSegModule(object):
    def __init__(self):
        workspace_seg = np.zeros([96, 96])
        workspace_seg[10:-10, 10:-10] = 1.0
        self.workspace_seg = workspace_seg

    def get_masks(self, color, depth, n_cluster=3):
        fmask = (depth < 0.625).astype(float)
        fmask[:5, :] = 0.0
        fmask[-5:, :] = 0.0
        fmask[:, :5] = 0.0
        fmask[:, -5:] = 0.0

        my, mx = np.nonzero(fmask)
        points = list(zip(mx, my, np.ones_like(mx) * 96))
        z = (np.array(points).T / np.linalg.norm(points, axis=1)).T

        im_blur = cv2.blur(color, (5, 5))
        colors = np.array([im_blur[y, x] / (10 * 255) for x, y in zip(mx, my)])
        z_color = np.concatenate([z, colors], 1)
        clusters = SpectralClustering(n_clusters=n_cluster, n_init=10).fit_predict(z_color)

        new_mask = np.zeros([fmask.shape[0], fmask.shape[1], n_cluster])
        for x, y, c in zip(mx, my, clusters):
            new_mask[y, x, c] = 1
        masks = new_mask.transpose([2,0,1]).astype(float)

        seg_colors = []
        for mask in masks:
            seg_color = color[mask.astype(bool)].mean(0) / 255.
            seg_colors.append(seg_color)

        return masks, np.array(seg_colors), fmask


class UR5Calibration(object):
    calib_positions = np.array([
        [0.0, -0.3, 0.65],
        [0.282, -0.413, 0.606],
        [0.249, -0.217, 0.567],
        [-0.193, -0.278, 0.495],
        [-0.249, -0.528, 0.45]
    ])
    # xyzw quaternion
    calib_quaternions = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.9917, 0.0041, -0.1246, 0.0321],
        [0.9626, 0.1529, -0.205, 0.09],
        [0.9697, -0.1399, 0.191, 0.0606],
        [0.9685, -0.1086, 0.2076, -0.0849]
    ])

    def __init__(self, ur5robot, method='leastsquares'):
        self.ur5 = ur5robot
        self.method = 'leastsquares'

        if self.method=='ukf':
            self.solve = self.calib_ukf
        elif self.method=='iekf':
            self.solve = self.calib_iekf
        else:
            self.solve = self.calib_leastsquares

    # for calibration
    def get_cam_theta_p(self, color, show_img=True):
        objpoints_rs, corners_rs = get_chessboard_corners(color)
        err_value, R_vec_cam_to_chess, p_cam_to_chess = cv2.solvePnP(objpoints_rs, corners_rs, K_rs, D_rs)
        img = cv2.drawChessboardCorners(np.array(color), CHECKERBOARD, corners_rs, True)
        if show_img:
            plt.imshow(img)
            plt.show()
        return R_vec_cam_to_chess, p_cam_to_chess

    def get_cam_R_T(self, color, show_img=True):
        objpoints_rs, corners_rs = get_chessboard_corners(color)
        img = cv2.drawChessboardCorners(np.array(color), CHECKERBOARD, corners_rs, True)
        if show_img:
            plt.imshow(img)
            plt.show()
        err_value, R_vec_cam_to_chess, p_cam_to_chess = cv2.solvePnP(objpoints_rs, corners_rs, K_rs, D_rs)
        R_cam_to_chess, _ = cv2.Rodrigues(R_vec_cam_to_chess)
        T_cam_to_chess = form_T(R_cam_to_chess, p_cam_to_chess)
        return R_cam_to_chess, T_cam_to_chess

    def get_calib_transformations(self):
        T_ur5 = []
        T_realsense = []

        for p, q in zip(self.calib_positions, self.calib_quaternions):
            img, _ = self.ur5.get_view(p, q)
            R, T_cam_to_chess = self.get_cam_R_T(img)
            T_chess_to_cam = np.linalg.inv(T_cam_to_chess)
            
            q_wxyz = [q[3], q[0], q[1], q[2]]
            T_base_to_eef = form_T(quaternion_matrix(q_wxyz)[:3, :3], p)
            
            T_ur5.append(T_base_to_eef)
            T_realsense.append(T_chess_to_cam)
            rospy.sleep(1.0)

        img, _ = self.ur5.get_view(self.ur5.ROBOT_INIT_POS)
        return T_ur5, T_realsense
    
    def form_AB_matrices(self, T_ur5, T_realsense):
        A = []
        B = []

        for i, Ti in enumerate(T_ur5):
            for j, Tj in enumerate(T_ur5):
                if i==j: continue
                A.append(np.linalg.inv(Ti).dot(Tj))
                
        for i, Ti in enumerate(T_realsense):
            for j, Tj in enumerate(T_realsense):
                if i==j: continue
                B.append(np.linalg.inv(Ti).dot(Tj))
                #A.append(Ti.dot(np.linalg.inv(Tj)))

        A = np.array(A).transpose([1,2,0])
        B = np.array(B).transpose([1,2,0])
        return A, B

    def get_calib_error(self, A, B, X):
        # A: T_ur5
        # B: T_realsense
        # X: T_eef_to_rs
        error = 0
        for i in range(A.shape[-1]):
            err = np.linalg.norm(A[:,:,i].dot(X) - X.dot(B[:,:,i]))
            error += err
        return error

    def calib_ukf(self, A, B):
        ukf=UKF()
        for i in range(len(A.shape[-1])):
            AA=A[:,:,i] 
            BB=B[:,:,i]
            ukf.Update(AA,BB)

        theta=np.linalg.norm(ukf.x[:3])
        if theta < EPS:
            k=[0,1,0] #VRML standard
        else:
            k=ukf.x[0:3]/np.linalg.norm(ukf.x[:3])
        euler_ukf=Tools.mat2euler(Tools.vec2rotmat(theta, k))
        print('.....UKF Results')

        print('Euler:', np.array(euler_ukf)*180/np.pi)
        print('Translation:', ukf.x[3:])
        print('------------------------------')
        T_eef_to_rs = form_T(Tools.vec2rotmat(theta, k), ukf.x[3:])
        print(T_eef_to_rs)

        print('------------------------------')
        print('Quat:', Rotation.from_matrix(T_eef_to_rs[:3,:3]).as_quat())
        print('Euler(degree):', Rotation.from_matrix(T_eef_to_rs[:3,:3]).as_euler('zyx', degrees=True))
        print('------------------------------')
        print('Error:', self.get_calib_error(T_eef_to_rs))
        return T_eef_to_rs

    def calib_iekf(self, A, B):
	#IEKF
        iekf=IEKF()
        for i in range(len(A.shape[-1])):
            AA=A[:,:,i] 
            BB=B[:,:,i]
            iekf.Update(AA,BB)
            
        theta=np.linalg.norm(iekf.x[:3])
        if theta < EPS:
            k=[0,1,0] #VRML standard
        else:
            k=iekf.x[0:3]/np.linalg.norm(iekf.x[:3])
        euler_iekf=Tools.mat2euler(Tools.vec2rotmat(theta, k))

        print('IEKF Results')

        print('Euler:', np.array(euler_iekf)*180/np.pi)
        print('Translation:', iekf.x[3:])
        print('------------------------------')
        T_eef_to_rs = form_T(Tools.vec2rotmat(theta, k), iekf.x[3:])
        print(T_eef_to_rs)

        print('------------------------------')
        print('Quat:', Rotation.from_matrix(T_eef_to_rs[:3,:3]).as_quat())
        print('Euler(degree):', Rotation.from_matrix(T_eef_to_rs[:3,:3]).as_euler('zyx', degrees=True))
        print('------------------------------')
        print('Error:', self.get_calib_error(T_eef_to_rs))
        return T_eef_to_rs

    def calib_leastsquares(self, A, B):
        T_eef_to_rs = LeastSquaresAXXB(A.transpose([2, 0, 1]), B.transpose([2, 0, 1]), verbose=True)

        print(T_eef_to_rs)
        print('------------------------------')
        print('Quat:', Rotation.from_matrix(T_eef_to_rs[:3,:3]).as_quat())
        print('Euler(degree):', Rotation.from_matrix(T_eef_to_rs[:3,:3]).as_euler('zyx', degrees=True))
        print('------------------------------')
        print('Error:', self.get_calib_error(T_eef_to_rs))
        return T_eef_to_rs

if __name__=='__main__':
    ur5robot = UR5Robot()
    color, depth = ur5robot.get_view()
    # plt.imshow(color)
    # plt.imshow(crop_image(color, 423, 251, 480))
    # plt.imshow(resize_image(crop_image(color, 423, 251, 480), 96, 96))
    # plt.imshow(resize_image(crop_image(depth, 423, 251, 480), 96, 96))

    realseg = RealSegModule()
    env = RealUR5Env(ur5robot, realseg, num_blocks=3)
    state = env.reset()

