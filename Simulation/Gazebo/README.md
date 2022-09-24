
RVIZ2是用来可视化数据的软件，核心要义是将数据展示出来, 不生产数据。 
而Gazebo是用于模拟真实环境生产数据的

Gazebo可以根据机器人模型文件，传感器配置参数，给机器人创造一个虚拟的环境，虚拟的电机和虚拟的传感器，
并通过ROS/ROS2的相关功能包把传感器数据电机数据等发送出来（生产数据）。

Gazebo 是一个独立的应用程序，可以独立于 ROS 或 ROS 2 使用。

Gazebo与ROS 版本的集成是通过一组叫做gazebo_ros_pkgs的包 完成的，gazebo_ros_pkgs将Gazebo和ROS2连接起来。

## gazebo_ros_pkgs
- gazebo_dev：开发Gazebo插件可以用的API
- gazebo_msgs：定义的ROS2和Gazebo之间的接口（Topic/Service/Action）
- gazebo_ros：提供方便的 C++ 类和函数，可供其他插件使用，例如转换和测试实用程序。它还提供了一些通常有用的插件。gazebo_ros::Node
- gazebo_plugins：一系列 Gazebo 插件，将传感器和其他功能暴露给 ROS2 例如:
    - gazebo_ros_camera 发布ROS2图像
    - gazebo_ros_diff_drive 通过ROS2控制和获取两轮驱动机器人的接口


