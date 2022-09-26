

## Reference

https://github.com/joshnewans/urdf_example

Getting Ready for ROS Part 7: Describing a robot with URDF
https://www.youtube.com/watch?v=CwdbsvcpOHM&list=PLunhqkrRNRhYYCaSTVP-qJnyUPkTxJnBt&index=7

https://articulatedrobotics.xyz/ready-for-ros-7-urdf/

Getting Ready for ROS Part 8: Simulating with Gazebo
https://articulatedrobotics.xyz/ready-for-ros-8-gazebo/


## Visulization

publish the robot description 
```
  ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_descdription:="$( xacro ~/my_robot.urdf.xacro )"
```

or use launch file
```
  ros2 launch urdf_viz rsp.launch.py
```

Open joint_state_publisher_gui to operat the robot
```
  ros2 run joint_state_publisher_gui joint_state_publisher_gui
```
Change the value of the joints


Visualize the state of robot
```
  rviz2
```
Set "fixed frame" to world

Add "TF", check "Show Names"

Add "RobotModel", set "Description Topic" to /robot_description, and alpha set to 0.8

## Simulate