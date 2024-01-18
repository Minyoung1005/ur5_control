#!/usr/bin/env python
import os
import sys
import rospy
import numpy as np

import actionlib
from robotiq_2f_gripper_msgs.msg import CommandRobotiqGripperFeedback, CommandRobotiqGripperResult, CommandRobotiqGripperAction, CommandRobotiqGripperGoal
from robotiq_2f_gripper_control.robotiq_2f_gripper_driver import Robotiq2FingerGripperDriver as Robotiq

sys.path.append(os.path.join('/home/dof6/catkin_ws/src/'))
#from moveit_tutorials.srv import *

from ur_msgs.srv import JointTrajectory, EndPose, JointStates
from moveit_msgs.msg import DisplayTrajectory
#from trajectory_msgs.msg import JointTrajectory

import moveit_commander
from geometry_msgs.msg import Pose
from moveit_commander import RobotCommander, MoveGroupCommander, roscpp_initialize

#group_name = "both_arms" #"left_arm", "both_arms"
#group = moveit_commander.MoveGroupCommander(group_name)

def get_joint_states(req):
    return str(robot_cmd.get_current_state().joint_state.position)

def get_eef_pose(req):
    return robot_cmd.get_link('tool0').pose().pose

def plan_robot_arm(req):
    if len(req.arm_qpos) != 0:
        #print(req.arm_qpos)
        arm_pose = dict(zip(req.arm_joint_name, req.arm_qpos))
        robot_arm.set_joint_value_target(arm_pose)
        plan_results = robot_arm.plan()
    elif len(req.arm_qpos) == 0:
        #print(req.eef_pose, req.eef_quat)
        pose_goal = Pose()
        pose_goal.orientation.x = req.eef_quat[0]
        pose_goal.orientation.y = req.eef_quat[1]
        pose_goal.orientation.z = req.eef_quat[2]
        pose_goal.orientation.w = req.eef_quat[3]
        pose_goal.position.x = req.eef_pose[0]
        pose_goal.position.y = req.eef_pose[1]
        pose_goal.position.z = req.eef_pose[2]

        (plan_results, fraction) = robot_arm.compute_cartesian_path([pose_goal], 0.01, 0.0)
        display_trajectory = DisplayTrajectory()
        display_trajectory.trajectory_start = robot_cmd.get_current_state()
        display_trajectory.trajectory.append(plan_results)
        display_trajectory_publisher.publish(display_trajectory)

    return plan_results.joint_trajectory

def move_robot_arm(req):
    if len(req.arm_qpos) != 0:
        #print(req.arm_qpos)
        arm_pose = dict(zip(req.arm_joint_name, req.arm_qpos))
        robot_arm.set_joint_value_target(arm_pose)
        plan_results = robot_arm.plan()
    elif len(req.arm_qpos) == 0:
        #print(req.eef_pose, req.eef_quat)
        #print(req.grasp)
        pose_goal = Pose()
        pose_goal.orientation.x = req.eef_quat[0]
        pose_goal.orientation.y = req.eef_quat[1]
        pose_goal.orientation.z = req.eef_quat[2]
        pose_goal.orientation.w = req.eef_quat[3]
        pose_goal.position.x = req.eef_pose[0]
        pose_goal.position.y = req.eef_pose[1]
        pose_goal.position.z = req.eef_pose[2]

        (plan_results, fraction) = robot_arm.compute_cartesian_path([pose_goal], 0.01, 0.0)
        display_trajectory = DisplayTrajectory()
        display_trajectory.trajectory_start = robot_cmd.get_current_state()
        display_trajectory.trajectory.append(plan_results)
        display_trajectory_publisher.publish(display_trajectory)

    robot_arm.execute(plan_results, wait=True)

    gripper_goal = CommandRobotiqGripperGoal()
    gripper_goal.emergency_release = False
    gripper_goal.stop = False
    gripper_goal.position = req.grasp
    gripper_goal.speed = 0.1
    gripper_goal.force = 5.0
    robotiq_client.send_goal(gripper_goal)
    robotiq_client.wait_for_result()

    return plan_results.joint_trajectory


def move_to_init_pose():
          
    """
    robot_arm.set_named_target("home")  #go to goal state.  robot_arm.go(wait=True)
    print("====== move plan go to home 1 ======")        
    rospy.sleep(1)  
    """      

    """robot_arm.set_named_target("up")  #go to goal state.
    robot_arm.go(wait=True)
    print("====== move plan go to up ======")        
    rospy.sleep(1)"""

    #robot_state = robot_arm.get_current_pose()
    #robot_angle = robot_arm.get_current_joint_values()

    pose_goal = Pose()
    pose_goal.orientation.x = 0.96
    pose_goal.orientation.y = -0.28
    pose_goal.orientation.z = 0.0
    pose_goal.orientation.w = -0.02
    pose_goal.position.x = 0.028
    pose_goal.position.y = -0.21
    pose_goal.position.z = 0.6

    (plan_results, fraction) = robot_arm.compute_cartesian_path([pose_goal], 0.01, 0.0)
    robot_arm.execute(plan_results, wait=True)

    '''
    #TARGET_JOINT_QPOS = [-1.9040511290179651, -1.9013617674456995, 1.276972770690918, -0.8737161795245569, 4.636346817016602, -3.311625067387716]
    TARGET_JOINT_QPOS = [-1.9631989637957972, -2.113516632710592, 1.476273536682129, -0.894970719014303, -1.5849650541888636, -2.9540748417318197]
    robot_arm.set_joint_value_target(TARGET_JOINT_QPOS)
    robot_arm.go(wait=True)
    rospy.sleep(1)  
    '''


if __name__ == '__main__':
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('ur5_move', anonymous=True)
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               DisplayTrajectory,
                                               queue_size=20)

    GROUP_NAME_ARM = "manipulator"
    robot_cmd = RobotCommander()
    robot_arm = MoveGroupCommander(GROUP_NAME_ARM)
    robot_arm.set_end_effector_link('tool0')

    action_name = rospy.get_param('~action_name', 'command_robotiq_action')
    robotiq_client = actionlib.SimpleActionClient(action_name, CommandRobotiqGripperAction)
    robotiq_client.wait_for_server()
    print("Client test: Starting sending goals")

    #move_to_init_pose()

    rospy.Service('get_joint_states', JointStates, get_joint_states)
    rospy.Service('get_eef_pose', EndPose, get_eef_pose)
    rospy.Service('plan_robot_arm', JointTrajectory, plan_robot_arm)
    rospy.Service('move_robot_arm', JointTrajectory, move_robot_arm)

    rospy.spin()





    




