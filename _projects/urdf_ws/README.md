

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

Open joint_state_publisher_gui to operate the robot
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

publish the robot description 
```
  ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_descdription:="$( xacro ~/my_robot.urdf.xacro )"
```
publish the robot description 
```
  ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_descdription:="$( xacro ~/my_robot.urdf.xacro )"
```
    ros2 launch gazebo_ros gazebo.lanucn.py
```

Spawn a robot
```
    ros2 ros2 launch gazebo_ros spawn_entity.py -topic robot_description --entity my_robot
```

Put them into launch file
```
  ros2 launch urdf_simu rsp_sim.launch.py
```
add pass "use_sim_time" to rotob_state_publiser



To add extra information to the URDF that is Gazebo-specific, we can add gazebo tags. 
Gazebo will use the content of these tags to generate its SDF files, but other things 
reading the URDF can just ignore them. 
These gazebo tags can reference a component of the URDF by name (i.e. a robot, link, or joint) using the syntax <gazebo reference="some_name">, or for things that are not linked to a component, but are relevant to the whole file we just use <gazebo>.

Append
```
<xacro:include filename="example_gazebo.xacro" />
```
to example_robot.urdf.xacro

Launch with world file
```
  ros2 launch urdf_simu rsp_sim.launch.py world:=worlds/test_world.world
```

## Simulate a camera

