# Odometry in ROS 2

In robotics, odometry is about using data from sensors to estimate the change in a robot’s position, orientation, and velocity over time relative to some point (e.g. x=0, y=0, z=0). 

Odometry information is normally obtained from sensors such as wheel encoders, IMU (Inertial measurement unit), and LIDAR. 


To correct for the inaccuracies of sensors, most ROS applications have an additional coordinate frame called `map` that provides globally accurate information and corrects drift that happens within the odom frame.