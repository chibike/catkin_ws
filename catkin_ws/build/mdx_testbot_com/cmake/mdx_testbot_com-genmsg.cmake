# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "mdx_testbot_com: 3 messages, 0 services")

set(MSG_I_FLAGS "-Imdx_testbot_com:/home/chibike/catkin_ws/src/mdx_testbot_com/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(mdx_testbot_com_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg" NAME_WE)
add_custom_target(_mdx_testbot_com_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mdx_testbot_com" "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg" ""
)

get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg" NAME_WE)
add_custom_target(_mdx_testbot_com_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mdx_testbot_com" "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg" ""
)

get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg" NAME_WE)
add_custom_target(_mdx_testbot_com_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "mdx_testbot_com" "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mdx_testbot_com
)
_generate_msg_cpp(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mdx_testbot_com
)
_generate_msg_cpp(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mdx_testbot_com
)

### Generating Services

### Generating Module File
_generate_module_cpp(mdx_testbot_com
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mdx_testbot_com
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(mdx_testbot_com_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(mdx_testbot_com_generate_messages mdx_testbot_com_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_cpp _mdx_testbot_com_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_cpp _mdx_testbot_com_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_cpp _mdx_testbot_com_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mdx_testbot_com_gencpp)
add_dependencies(mdx_testbot_com_gencpp mdx_testbot_com_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mdx_testbot_com_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mdx_testbot_com
)
_generate_msg_eus(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mdx_testbot_com
)
_generate_msg_eus(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mdx_testbot_com
)

### Generating Services

### Generating Module File
_generate_module_eus(mdx_testbot_com
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mdx_testbot_com
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(mdx_testbot_com_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(mdx_testbot_com_generate_messages mdx_testbot_com_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_eus _mdx_testbot_com_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_eus _mdx_testbot_com_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_eus _mdx_testbot_com_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mdx_testbot_com_geneus)
add_dependencies(mdx_testbot_com_geneus mdx_testbot_com_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mdx_testbot_com_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mdx_testbot_com
)
_generate_msg_lisp(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mdx_testbot_com
)
_generate_msg_lisp(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mdx_testbot_com
)

### Generating Services

### Generating Module File
_generate_module_lisp(mdx_testbot_com
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mdx_testbot_com
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(mdx_testbot_com_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(mdx_testbot_com_generate_messages mdx_testbot_com_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_lisp _mdx_testbot_com_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_lisp _mdx_testbot_com_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_lisp _mdx_testbot_com_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mdx_testbot_com_genlisp)
add_dependencies(mdx_testbot_com_genlisp mdx_testbot_com_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mdx_testbot_com_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mdx_testbot_com
)
_generate_msg_nodejs(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mdx_testbot_com
)
_generate_msg_nodejs(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mdx_testbot_com
)

### Generating Services

### Generating Module File
_generate_module_nodejs(mdx_testbot_com
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mdx_testbot_com
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(mdx_testbot_com_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(mdx_testbot_com_generate_messages mdx_testbot_com_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_nodejs _mdx_testbot_com_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_nodejs _mdx_testbot_com_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_nodejs _mdx_testbot_com_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mdx_testbot_com_gennodejs)
add_dependencies(mdx_testbot_com_gennodejs mdx_testbot_com_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mdx_testbot_com_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mdx_testbot_com
)
_generate_msg_py(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mdx_testbot_com
)
_generate_msg_py(mdx_testbot_com
  "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mdx_testbot_com
)

### Generating Services

### Generating Module File
_generate_module_py(mdx_testbot_com
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mdx_testbot_com
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(mdx_testbot_com_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(mdx_testbot_com_generate_messages mdx_testbot_com_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/Num.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_py _mdx_testbot_com_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/AudioData.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_py _mdx_testbot_com_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/mdx_testbot_com/msg/VideoData.msg" NAME_WE)
add_dependencies(mdx_testbot_com_generate_messages_py _mdx_testbot_com_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(mdx_testbot_com_genpy)
add_dependencies(mdx_testbot_com_genpy mdx_testbot_com_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS mdx_testbot_com_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mdx_testbot_com)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/mdx_testbot_com
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(mdx_testbot_com_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mdx_testbot_com)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/mdx_testbot_com
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(mdx_testbot_com_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mdx_testbot_com)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/mdx_testbot_com
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(mdx_testbot_com_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mdx_testbot_com)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/mdx_testbot_com
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(mdx_testbot_com_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mdx_testbot_com)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mdx_testbot_com\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/mdx_testbot_com
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(mdx_testbot_com_generate_messages_py std_msgs_generate_messages_py)
endif()
