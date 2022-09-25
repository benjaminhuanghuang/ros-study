https://classic.gazebosim.org/tutorials?tut=install_ubuntu


## Install
```
curl -sSL http://get.gazebosim.org | sh
```

gazebo是独立于ROS/ROS2之外的仿真软件，可以独立Gazebo。如果要通过ROS2和Gazebo进行交互，需要gazebo_ros插件来进行。
```
sudo apt install ros-humble-gazebo-ros

sudo apt install ros-humble-gazebo-*
```


## Run
```
gazebo

or

ros2 launch gazebo_ros gazebo.launch.py
```

Start gazebo and load ROS2 addins
```
gazebo --verbose -s libgazebo_ros_factory.so
```

Check Gazebo version

```
dpkg -l | grep gazebo
```