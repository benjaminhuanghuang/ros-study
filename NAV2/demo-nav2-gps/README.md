# How to Use GPS With the Robot Localization Package – ROS 2
https://automaticaddison.com/how-to-use-gps-with-the-robot-localization-package-ros-2/


## dependencies in package.xml
```
  <buildtool_depend>ament_cmake</buildtool_depend>
  
  <exec_depend>joint_state_publisher</exec_depend>
  <exec_depend>robot_localization</exec_depend>
  <exec_depend>robot_state_publisher</exec_depend>
  <exec_depend>rviz</exec_depend>
  <exec_depend>xacro</exec_depend>
```


## Build
```
colcon build --packages-select basic_mobile_robot
```

## Launch
```
ros2 launch basic_mobile_robot basic_mobile_bot_v6.launch.py
```