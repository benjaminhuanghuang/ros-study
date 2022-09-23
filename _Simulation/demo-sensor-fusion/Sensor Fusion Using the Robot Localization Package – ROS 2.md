# Sensor Fusion Using the Robot Localization Package – ROS2

We will use the robot_localization package to fuse odometry data from the /wheel/odometry topic with IMU data from the /imu/data topic to provide locally accurate, smooth odometry estimates. Wheels can slip, so using the robot_localization package can help correct for this.

We will configure the robot_localization package to use an Extended Kalman Filter (ekf_node) to fuse the data from sensor inputs.



