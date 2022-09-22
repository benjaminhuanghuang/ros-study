
https://navigation.ros.org/build_instructions/index.html


```
# install
sudo apt install ros-<distro>-navigation2 ros-<distro>-nav2-bringup ros-<distro>-turtlebot3*

# ubuntu 20.04
sudo apt install ros-<distro>-navigation2 ros-<distro>-nav2-bringup '~ros-<distro>-turtlebot3-.*'

# my evn
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup '~ros-humble-turtlebot3-.*'

sudo apt-get install ros-humble-gazebo-*

```

Install TurtleBot3 via Debian Packages
```
sudo apt install ros-<distro>-turtlebot3

# my evn
sudo apt install ros-humble-turtlebot3

```

Set environment variable
```
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models
```



```
ros2 launch nav2_bringup tb3_simulation_launch.py
```
这个启动文件会在turtlebot3_world仿真世界中启动带有AMCL定位程序的Nav2软件包。
同时还会启动机器人状态发布者节点以提供坐标变换、一个含有Turtlebot3 URDF模型的Gazebo实例和RVIZ。
如果一切正常，就可以看到RViz和Gazebo GUI

Install package if you see error "package 'gazebo_ros' not found"
```
sudo apt install ros-humble-gazebo-ros-pkgs
```