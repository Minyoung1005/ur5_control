# Install script for directory: /home/dof6/catkin_ws/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/dof6/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/dof6/catkin_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/dof6/catkin_ws/install" TYPE PROGRAM FILES "/home/dof6/catkin_ws/build/catkin_generated/installspace/_setup_util.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/dof6/catkin_ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/dof6/catkin_ws/install" TYPE PROGRAM FILES "/home/dof6/catkin_ws/build/catkin_generated/installspace/env.sh")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/dof6/catkin_ws/install/setup.bash;/home/dof6/catkin_ws/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/dof6/catkin_ws/install" TYPE FILE FILES
    "/home/dof6/catkin_ws/build/catkin_generated/installspace/setup.bash"
    "/home/dof6/catkin_ws/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/dof6/catkin_ws/install/setup.sh;/home/dof6/catkin_ws/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/dof6/catkin_ws/install" TYPE FILE FILES
    "/home/dof6/catkin_ws/build/catkin_generated/installspace/setup.sh"
    "/home/dof6/catkin_ws/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/dof6/catkin_ws/install/setup.zsh;/home/dof6/catkin_ws/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/dof6/catkin_ws/install" TYPE FILE FILES
    "/home/dof6/catkin_ws/build/catkin_generated/installspace/setup.zsh"
    "/home/dof6/catkin_ws/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/dof6/catkin_ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/dof6/catkin_ws/install" TYPE FILE FILES "/home/dof6/catkin_ws/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/dof6/catkin_ws/build/gtest/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/easy_handeye/easy_handeye/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/robotiq_2finger_grippers/robotiq_2f_140_gripper_visualization/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/robotiq_2finger_grippers/robotiq_2f_85_gripper_visualization/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/realsense-ros/realsense2_description/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/easy_handeye/rqt_easy_handeye/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/easy_handeye/easy_handeye_msgs/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/marker_msgs-master/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_marker_detection/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/universal_robot/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/universal_robots/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/ur5/ur5_description/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/ur5/ur5_gazebo/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/Universal_Robots_ROS_Driver/ur_dashboard_msgs/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur_description/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur_e_description/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur_msgs/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/autolab_core/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/Universal_Robots_ROS_Driver/controller_stopper/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/robotiq/robotiq_description/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/robotiq_2finger_grippers/robotiq_modbus_rtu/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/robotiq_2finger_grippers/robotiq_2f_gripper_msgs/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/robotiq_2finger_grippers/robotiq_2f_gripper_control/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/realsense-ros/realsense2_camera/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/robotiq_2finger_grippers/robotiq_2f_85_gripper_gazebo/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/robotiq/robotiq_gazebo/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_aruco/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_checkerboard/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_ellipses/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_marker_pose_estimation/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur_bringup/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/Universal_Robots_ROS_Driver/ur_calibration/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur_driver/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur_e_gazebo/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur_gazebo/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur_kinematics/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/vision_msgs-kinetic-devel/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur10_e_moveit_config/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur10_moveit_config/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur3_e_moveit_config/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur3_moveit_config/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur5_e_moveit_config/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/fmauch_universal_robot/ur5_moveit_config/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/ur5_robotiq_moveit/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/Universal_Robots_ROS_Driver/ur_controllers/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/Universal_Robots_ROS_Driver/ur_robot_driver/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/dof6/catkin_ws/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
