# Install script for directory: /home/dof6/catkin_ws/src/tuw_marker_detection-kinetic-devel/tuw_aruco/aruco-2.0.10

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
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake" TYPE FILE FILES "/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_aruco/aruco-2.0.10/Findaruco.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES
    "/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_aruco/aruco-2.0.10/aruco-uninstalled.pc"
    "/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_aruco/aruco-2.0.10/aruco.pc"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_aruco/aruco-2.0.10/src/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_aruco/aruco-2.0.10/utils/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_aruco/aruco-2.0.10/utils_markermap/cmake_install.cmake")
  include("/home/dof6/catkin_ws/build/tuw_marker_detection-kinetic-devel/tuw_aruco/aruco-2.0.10/utils_calibration/cmake_install.cmake")

endif()

