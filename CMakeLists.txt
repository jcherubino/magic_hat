cmake_minimum_required(VERSION 2.8.3)
project(magic_hat)

#Get information about this package's buildtime dependencies
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  message_generation
)

## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   TurtleInfo.msg
 )

## Generate added messages and services with any dependencies listed here
generate_messages(DEPENDENCIES ${PROJECT_NAME})

#Declare this catkin package's runtime dependencies
catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS roscpp rospy  message_runtime
)

include_directories(
include
 ${catkin_INCLUDE_DIRS}
)

#define executable using TurtleInfo.msg
add_executable(subscriber src/subscriber.cpp)

#specify which libraries an executable target links against.
target_link_libraries(subscriber ${catkin_LIBRARIES})

add_dependencies(subscriber ${${PROJECT_NAME}_EXPORTED_TARGETS})
