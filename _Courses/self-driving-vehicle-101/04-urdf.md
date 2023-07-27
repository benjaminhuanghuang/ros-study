# URDF (Unified Robot Description format)

1. Create package
```
    ros2 pkg create box
```


2. Create urdf


3. Create launch

How to Load a URDF File into Gazebo – ROS 2
https://automaticaddison.com/how-to-load-a-urdf-file-into-gazebo-ros-2/



4. Modify CMakeLists.txt
```
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)
```

## Run
publish the robot description 
```
  ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_descdription:="$( xacro ~/my_robot.urdf.xacro )"
```

or use launch file
```
  ros2 launch box spawn_box.launch.py
```

Open joint_state_publisher_gui to operat the robot
```
  ros2 run joint_state_publisher_gui joint_state_publisher_gui
```

Visualize the state of robot
```
  rviz2
```