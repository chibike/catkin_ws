# Install script for directory: /home/chibike/catkin_ws/src/see_n_tell

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/chibike/catkin_ws/install")
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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/see_n_tell/msg" TYPE FILE FILES
    "/home/chibike/catkin_ws/src/see_n_tell/msg/UInt8Array.msg"
    "/home/chibike/catkin_ws/src/see_n_tell/msg/UInt16Array.msg"
    "/home/chibike/catkin_ws/src/see_n_tell/msg/UInt32Array.msg"
    "/home/chibike/catkin_ws/src/see_n_tell/msg/Int32Array.msg"
    "/home/chibike/catkin_ws/src/see_n_tell/msg/Float32Array.msg"
    "/home/chibike/catkin_ws/src/see_n_tell/msg/Float64Array.msg"
    "/home/chibike/catkin_ws/src/see_n_tell/msg/ContourData.msg"
    "/home/chibike/catkin_ws/src/see_n_tell/msg/TaggedObjects.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/see_n_tell/cmake" TYPE FILE FILES "/home/chibike/catkin_ws/build/see_n_tell/catkin_generated/installspace/see_n_tell-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/chibike/catkin_ws/devel/include/see_n_tell")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/chibike/catkin_ws/devel/share/roseus/ros/see_n_tell")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/chibike/catkin_ws/devel/share/common-lisp/ros/see_n_tell")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/chibike/catkin_ws/devel/share/gennodejs/ros/see_n_tell")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/chibike/catkin_ws/devel/lib/python2.7/dist-packages/see_n_tell")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/chibike/catkin_ws/devel/lib/python2.7/dist-packages/see_n_tell")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/chibike/catkin_ws/build/see_n_tell/catkin_generated/installspace/see_n_tell.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/see_n_tell/cmake" TYPE FILE FILES "/home/chibike/catkin_ws/build/see_n_tell/catkin_generated/installspace/see_n_tell-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/see_n_tell/cmake" TYPE FILE FILES
    "/home/chibike/catkin_ws/build/see_n_tell/catkin_generated/installspace/see_n_tellConfig.cmake"
    "/home/chibike/catkin_ws/build/see_n_tell/catkin_generated/installspace/see_n_tellConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/see_n_tell" TYPE FILE FILES "/home/chibike/catkin_ws/src/see_n_tell/package.xml")
endif()

