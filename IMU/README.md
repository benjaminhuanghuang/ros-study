# IMU (Inertial Measurement Unit) 
It has a gyro and accelerometer and a magnetometer.
惯性测量单元是测量物体三轴姿态角(或角速率)以及加速度的装置。一般的，一个IMU包含了三个单轴的加速度计和三个单轴的陀螺，加速度计检测物体在载体坐标系统独立三轴的加速度信号，而陀螺检测载体相对于导航坐标系的角速度信号，测量物体在三维空间中的角速度和加速度，并以此解算出物体的姿态。

IMU可以测量以下三组数据：

三维角度
三维加速度
三维角速度


仿真的IMU对应一个后缀为.so的动态链接库，使用下面的指令可以查看所有的动态链接库：

```
ls /opt/ros/foxy/lib/libgazebo_ros*
```

IMU对应的消息类型为sensor_msgs/msg/Imu
```
    ros2 interface show sensor_msgs/msg/Imu
```

Check message
```
ros2 topic list
ros2 topic info /imu
Copy to clipboardErrorCopied
ros2 topic echo /imu
```