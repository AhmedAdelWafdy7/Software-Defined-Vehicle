cmake_minimum_required(VERSION 3.0.2)
project(sdv_sensors)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs sensor_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/camera_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
) 