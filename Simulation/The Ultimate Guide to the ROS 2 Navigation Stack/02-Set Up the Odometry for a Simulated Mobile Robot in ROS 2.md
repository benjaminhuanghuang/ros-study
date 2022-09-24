# Set Up the Odometry for a Simulated Mobile Robot in ROS 2
https://automaticaddison.com/set-up-the-odometry-for-a-simulated-mobile-robot-in-ros-2/


In robotics, odometry is about using data from sensors to estimate the change in a robot’s position, orientation, and velocity over time relative to some point (e.g. x=0, y=0, z=0). 

Odometry information is normally obtained from sensors such as wheel encoders, IMU (Inertial measurement unit), and LIDAR. 


To correct for the inaccuracies of sensors, most ROS applications have an additional coordinate frame called `map` that provides globally accurate information and corrects drift that happens within the odom frame.


## Prerequisites
gazebo


## Setup 
```
sudo apt-get update
sudo apt-get upgrade
sudo apt install ros-humble-gazebo-ros-pkgs
```

## Create a SDF file 
we need to use an SDF file for Gazebo stuff and a URDF file for ROS stuff.

```
cd workspace/src/basic_mobile_robot/models/

mkdir basic_mobile_bot_description

cd basic_mobile_bot_description

touch model.config
```
The links of the mobile robot include the robot base (often called “chassis”), the two drive wheels, the front caster wheel, the IMU, and the GPS.


## Add mesh files
```
cd workspace/src/basic_mobile_robot/models/basic_mobile_bot_description

mkdir meshes

```
https://drive.google.com/drive/folders/1_33gXeb-VelnJLc2t4JfmaEDApzbn9fm


## Add the Path of the Model to the Bashrc File
Make sure gazebo can find the model (Insert tab)

Add the following line to the bottom of the bashrc file:
```
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/ben/workspace/odometry_ws/src/basic_mobile_robot/models/
```

## Test robot
```
sudo apt install ros-humble-rqt-robot-steering

rqt_robot_steering
```

## Create an SDF File for the World
```
cd workspace/src/basic_mobile_robot/worlds/

mkdir basic_mobile_bot_world

cd basic_mobile_bot_world

touch smalltown.world
```

The world file has 6 sections:
Place objects in the world
Define the lighting of the world
Define the physics of the world
Define the latitude, longitude, and elevation
Define the user perspective of the world (i.e. aerial view)
Import our own robot