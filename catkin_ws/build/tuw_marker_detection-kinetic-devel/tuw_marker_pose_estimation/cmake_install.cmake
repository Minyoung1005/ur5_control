# Install script for directory: /home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_marker_pose_estimation

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/tuw_marker_pose_estimation" TYPE FILE FILES "/home/dof6/catkin_ws/devel/include/tuw_marker_pose_estimation/MarkerPoseEstimationConfig.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/tuw_marker_pose_estimation" TYPE FILE FILES "/home/dof6/catkin_ws/devel/include/tuw_marker_pose_estimation/MarkerMapPoseEstimationConfig.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/tuw_marker_pose_estimation" TYPE FILE FILES "/home/dof6/catkin_ws/devel/lib/python2.7/dist-packages/tuw_marker_pose_estimation/__init__.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/dof6/catkin_ws/devel/lib/python2.7/dist-packages/tuw_marker_pose_estimation/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/tuw_marker_pose_estimation" TYPE DIRECTORY FILES "/home/dof6/catkin_ws/devel/lib/python2.7/dist-packages/tuw_marker_pose_estimation/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_marker_pose_estimation/catkin_generated/installspace/tuw_marker_pose_estimation.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tuw_marker_pose_estimation/cmake" TYPE FILE FILES
    "/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_marker_pose_estimation/catkin_generated/installspace/tuw_marker_pose_estimationConfig.cmake"
    "/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_marker_pose_estimation/catkin_generated/installspace/tuw_marker_pose_estimationConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/tuw_marker_pose_estimation" TYPE FILE FILES "/home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_marker_pose_estimation/package.xml")
endif()

