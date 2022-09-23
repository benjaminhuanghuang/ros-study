# Sensor Fusion Using the Robot Localization Package – ROS2

We will use the robot_localization package to fuse odometry data from the /wheel/odometry topic with IMU data from the /imu/data topic to provide locally accurate, smooth odometry estimates. Wheels can slip, so using the robot_localization package can help correct for this.

We will configure the robot_localization package to use an Extended Kalman Filter (ekf_node) to fuse the data from sensor inputs.


These sensor inputs come from the IMU Gazebo plugin and the differential drive Gazebo plugin that are defined in our SDF file.

In a real robotics project, instead of simulated IMU and odometry data, we would use data from an IMU sensor like the BNO055 and wheel encoders, respectively.

The ekf_node will subscribe to the following topics (ROS message types are in parentheses):

- /wheel/odometry :  Position and velocity estimate based on the information from the differential drive Gazebo plugin (in a real robotics project this would be information drawn from wheel encoder tick counts). The orientation is in quaternion format. (nav_msgs/Odometry)

- /imu/data : Data from the Inertial Measurement Unit (IMU) sensor Gazebo plugin (sensor_msgs/Imu.msg)
This node will publish data to the following topics:

- /odometry/filtered : The smoothed odometry information (nav_msgs/Odometry)

- /tf : Coordinate transform from the odom frame (parent) to the base_footprint frame (child). To learn about coordinate frames in ROS, check out this post.

Install Robot Localization Package
```
sudo apt install ros-humble-robot-localization
```

Set the Configuration Parameters
```
cd workspace/src/basic_mobile_robot/config/

touch ekf.yaml
```
https://drive.google.com/file/d/1dabLo4qQEw4k-Nbyfkf0niwCBprt1lIt/view?usp=sharing


Create Launch file
https://drive.google.com/file/d/1gGGRX1LstBj6Xlf3gb8sRloHKKzywCJQ/view?usp=sharing


Modify package.xml

```
  <exec_depend>joint_state_publisher</exec_depend>
  <exec_depend>robot_localization</exec_depend>
  <exec_depend>robot_state_publisher</exec_depend>
  <exec_depend>rviz</exec_depend>
  <exec_depend>xacro</exec_depend>
```

Modify CMakeLists.txt
https://drive.google.com/file/d/1Fr5YZZ-AfHgHUXmbimvBFEn6UF57ovhN/view?usp=sharing


Build
```
cd workspace

colcon build
```

Launch
```
ros2 launch basic_mobile_robot basic_mobile_bot_v3.launch.py headless:=False
```

To see the output of the robot localization package (i.e. the Extended Kalman Filter (EKF)
```
ros2 topic echo /odometry/filtered
```


move robot
```
rqt_robot_steering
```

We can see the output of the odom -> base_footprint transform by typing the following command:
```
ros2 run tf2_ros tf2_echo odom base_footprint
```

check out the ekf_node (named ekf_filter_node).
```
ros2 node info /ekf_filter_node
```

check out the ROS node graph.
```
rqt_grap
```