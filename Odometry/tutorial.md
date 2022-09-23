# Set Up the Odometry for a Simulated Mobile Robot in ROS 2
https://automaticaddison.com/set-up-the-odometry-for-a-simulated-mobile-robot-in-ros-2/


## Prerequisites
gazebo


## Setup 
```
sudo apt-get update
sudo apt-get upgrade
sudo apt install ros-humble-gazebo-ros-pkgs
```

Create a SDF file for Gazebo
```
cd workspace/src/basic_mobile_robot/models/

mkdir basic_mobile_bot_description

cd basic_mobile_bot_description

touch model.config
```

! Add the Path of the Model to the Bashrc File
```
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/ben/workspace/odometry_ws/src/basic_mobile_robot/models/
```

Create an SDF File for the World
```
cd workspace/src/basic_mobile_robot/worlds/

mkdir basic_mobile_bot_world

cd basic_mobile_bot_world

touch smalltown.world
```