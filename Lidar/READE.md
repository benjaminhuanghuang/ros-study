# LiDAR(Light Detection And Ranging）
激光 探测 测距


激光雷达是属于射线类传感器, 该类传感在在Gazebo插件中都被封装成了一个动态库libgazebo_ros_ray_sensor.so。

Interface of LiDAR Topic
```
ros2 interface show sensor_msgs/msg/LaserScan
```

Check message
```
ros2 topic list
ros2 topic info /scan

ros2 topic echo /scan
```