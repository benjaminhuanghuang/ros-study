# How to Create a Simulated Mobile Robot in ROS 2 Using URDF

https://automaticaddison.com/how-to-create-a-simulated-mobile-robot-in-ros-2-using-urdf/

A URDF (Universal Robot Description Format) file is an XML file that describes what a robot should look like in real life



## Install ROS2 packages
```
sudo apt install ros-<ros2-distro>-joint-state-publisher-gui
sudo apt install ros-<ros2-distro>-xacro
```
for example
```
sudo apt install ros-humble-joint-state-publisher-gui
sudo apt install ros-humble-xacro
```


## Create package
```
cd workspace/src

ros2 pkg create --build-type ament_cmake ben_robot

cd workspace/src/ben_robot

mkdir config launch maps meshes models params rviz worlds
```

## Build
```
cd workspace/

colcon build
```

## Add URDF file

All robots are made up of links and joints. 

The links of the mobile robot include the robot base (often called “chassis”), the two drive wheels, the front caster wheel, the IMU, and the GPS.

We also have a virtual link known as the base footprint. The base footprint (as shown on this post) is the link directly under the center of the robot.

```
cd workspace/src/ben_robot/models

touch basic_mobile_bot_v1.urdf

```
https://drive.google.com/file/d/1UNBKEZWsgo3cp1XBgdU3UY8TGRS-fMK9/view?usp=sharing


## Add meshes file
```
cd workspace/src/basic_mobile_robot/meshes

```

## Add Dependencies into package.xml
```
  <exec_depend>joint_state_publisher</exec_depend>
  <exec_depend>robot_state_publisher</exec_depend>
  <exec_depend>rviz</exec_depend>
  <exec_depend>xacro</exec_depend>
```
We will be using the Joint State Publisher and the Robot State Publisher.

We will also be using RViz to visualize our robot model.


## Create the Launch File
This launch file will be used by ROS2 to load the necessary nodes for our package. 

```
cd workspace/src/basic_mobile_robot/launch/

touch ben_robot.launch.py
```

LaunchConfiguration variables:
```
# Launch configuration variables specific to simulation
gui = LaunchConfiguration('gui')
model = LaunchConfiguration('model')
rviz_config_file = LaunchConfiguration('rviz_config_file')
use_robot_state_pub = LaunchConfiguration('use_robot_state_pub')
use_rviz = LaunchConfiguration('use_rviz')
use_sim_time = LaunchConfiguration('use_sim_time')
```
These variables are options for how we want to launch our robot simulation. 


## Add RViz Configuration File
```
cd workspace/src/basic_mobile_robot/rviz/

touch urdf_config.rviz
```
https://drive.google.com/drive/folders/1I9msYUB1s7Pf6ZuSIrsFlMQuptLlBU86



## Modify CMakeLists.txt
```
install(
  DIRECTORY config launch maps meshes models params rviz src worlds
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
...

```

## Launch robot
```
ros2 launch ben_robot ben_robot.launch.py

# see the available arguments you can pass to the launch file
ros2 launch -s basic_mobile_robot basic_mobile_bot_v1.launch.py
```
