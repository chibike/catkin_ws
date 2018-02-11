#!/bin/bash

package_name=rover_simulation_pkg
workspace_name=catkin_ws

cd ~/$workspace_name/src
catkin_create_pkg $package_name std_msgs rospy roscpp
cd ~/$workspace_name
catkin_make
.~/$workspace_name/devel/setup.bash

source /opt/ros/kinetic/setup.bash
catkin_make
catkin_make install

cd ~/$workspace_name/
catkin_make


