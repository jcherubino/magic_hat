cmake_minimum_required(VERSION 2.8.3)
project(magic_hat)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  message_generation
)

add_message_files(FILES TurtleInfo.msg)

generate_messages(DEPENDENCIES ${PROJECT_NAME})

catkin_package(
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS roscpp rospy message_runtime
)

include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(subscriber src/subscriber.cpp)
add_dependencies(subscriber ${${PROJECT_NAME}_EXPORTED_TARGETS})
target_link_libraries(subscriber ${catkin_LIBRARIES})
