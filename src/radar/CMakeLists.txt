cmake_minimum_required(VERSION 3.0.2)
project(radar)
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)
add_message_files(
    FILES
    radar_message.msg
)
generate_messages(DEPENDENCIES std_msgs)
catkin_package(
   #INCLUDE_DIRS include
   LIBRARIES radar
   CATKIN_DEPENDS rospy std_msgs
   #DEPENDS system_lib
)

catkin_install_python(PROGRAMS
    src/RadarPassing.py
    src/RadarDataStore.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
