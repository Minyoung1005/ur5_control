# Dependencies

```
rosdep install --from-paths src --ignore-src -r -y
```
Install Universal_Robots_ROS_Driver: https://github.com/UniversalRobots/Universal_Robots_ROS_Driver

Check the connection port after connecting Robotiq Gripper and PC

Check /dev/ttyUSB* and if it's not ttyUSB0, modify the comport argument in “robotiq_2finger_grippers/robotiq_2f_gripper_control/launch/robotiq_action_server.launch”

usb port problem: https://github.com/ros-industrial/robotiq/issues/167


# gripper usb connection

```
roslaunch robotiq_2f_gripper_control robotiq_action_server.launch
```


gripper open close topic name: /command_robotiq_action/goal

position: 0 close gripper position: 1 open gripper


# robot connection

```
roslaunch ur_robot_driver ur5_robotiq_bringup.launch robot_ip:=192.168.60.31
( roslaunch ur_robot_driver ur5_bringup.launch robot_ip:=192.168.60.31 )
```

# moveit
```
roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch
```

# rviz
```
roslaunch ur5_moveit_config moveit_rviz.launch config:=true
```

# controller

```
rosrun rqt_joint_trajectory_controller rqt_joint_trajectory_controller 
```


# realsense camera

```
roslaunch realsense2_camera rs_camera.launch filters:=pointcloud
```


# checkerboard tracker

```
rosrun tuw_checkerboard tuw_checkerboard_node image:=/camera/color/image_raw camera_info:=/camera/color/camera_info
```

# tutorial
1. Power On
2. Press Start
3. (Optional) Press the button behind the controller to manually move the joints (push hard)
4. Press OK on bottom right
5. Run Program -> File on the top left -> Load Program
6. Select external_control.urp and Press Open
7. Press the green button to start
8. Execute the following commands in different terminals (or just use different panes in tmux)

```
# 1st terminal
$ roslaunch ur_robot_driver ur5_robotiq_bringup.launch robot_ip:=192.168.60.31

# 2nd terminal
$ roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch
# "We can start planning now!" will appear if successful

# press start - external control

# (Optional) 3rd terminal
$ roslaunch ur5_moveit_config moveit_rviz.launch config:=true
# manual control in rviz
# control using the arrows
# (Important) First Plan, then Execute! (avoid collision)
# quit rviz and run
$ rosrun rqt_joint_trajectory_controller rqt_joint_trajectory_controller

# 4th terminal
ur5/realrobot$ python planner.py # fix path to catkin_ws/src/ in the code

# calibration
# execute ur5/realrobot/Calibration Manual.ipynb
```