# Universal Robot Description Format (URDF)

A URDF (Universal Robot Description Format) file is an XML file that describes what a robot should look like in real life


The body of a robot consists of two components:
- Links are connected to each other by joints.
- Joints are the pieces of the robot that move, enabling motion between connected links.

robotic arm is made of rigid pieces (links) and non-rigid pieces (joints).
Servo motors at the joints cause the links of a robotic arm to move.


## Setup
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
```
cd workspace/src/ben_robot/model

```

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
```
cd workspace/src/basic_mobile_robot/launch/

touch ben_robot.launch.py
```


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
ros2 launch basic_mobile_robot basic_mobile_bot_v1.launch.py

# see the available arguments you can pass to the launch file
ros2 launch -s basic_mobile_robot basic_mobile_bot_v1.launch.py
```