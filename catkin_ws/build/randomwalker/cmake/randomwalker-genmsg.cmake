# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "randomwalker: 0 messages, 2 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(randomwalker_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv" NAME_WE)
add_custom_target(_randomwalker_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "randomwalker" "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv" ""
)

get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv" NAME_WE)
add_custom_target(_randomwalker_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "randomwalker" "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(randomwalker
  "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/randomwalker
)
_generate_srv_cpp(randomwalker
  "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/randomwalker
)

### Generating Module File
_generate_module_cpp(randomwalker
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/randomwalker
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(randomwalker_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(randomwalker_generate_messages randomwalker_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_cpp _randomwalker_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_cpp _randomwalker_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(randomwalker_gencpp)
add_dependencies(randomwalker_gencpp randomwalker_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS randomwalker_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(randomwalker
  "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/randomwalker
)
_generate_srv_eus(randomwalker
  "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/randomwalker
)

### Generating Module File
_generate_module_eus(randomwalker
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/randomwalker
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(randomwalker_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(randomwalker_generate_messages randomwalker_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_eus _randomwalker_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_eus _randomwalker_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(randomwalker_geneus)
add_dependencies(randomwalker_geneus randomwalker_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS randomwalker_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(randomwalker
  "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/randomwalker
)
_generate_srv_lisp(randomwalker
  "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/randomwalker
)

### Generating Module File
_generate_module_lisp(randomwalker
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/randomwalker
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(randomwalker_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(randomwalker_generate_messages randomwalker_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_lisp _randomwalker_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_lisp _randomwalker_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(randomwalker_genlisp)
add_dependencies(randomwalker_genlisp randomwalker_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS randomwalker_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(randomwalker
  "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/randomwalker
)
_generate_srv_nodejs(randomwalker
  "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/randomwalker
)

### Generating Module File
_generate_module_nodejs(randomwalker
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/randomwalker
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(randomwalker_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(randomwalker_generate_messages randomwalker_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_nodejs _randomwalker_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_nodejs _randomwalker_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(randomwalker_gennodejs)
add_dependencies(randomwalker_gennodejs randomwalker_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS randomwalker_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(randomwalker
  "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker
)
_generate_srv_py(randomwalker
  "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker
)

### Generating Module File
_generate_module_py(randomwalker
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(randomwalker_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(randomwalker_generate_messages randomwalker_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetScore.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_py _randomwalker_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/chibike/catkin_ws/src/randomwalker/srv/GetBounds.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_py _randomwalker_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(randomwalker_genpy)
add_dependencies(randomwalker_genpy randomwalker_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS randomwalker_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/randomwalker)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/randomwalker
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(randomwalker_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/randomwalker)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/randomwalker
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(randomwalker_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/randomwalker)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/randomwalker
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(randomwalker_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/randomwalker)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/randomwalker
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(randomwalker_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(randomwalker_generate_messages_py std_msgs_generate_messages_py)
endif()
