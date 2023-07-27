

Use ROS2 Humble + Ubuntu 20.04

```
sudo apt install ros-humble-desktop

sudo apt install ros-humble-ros-base
```

The install path:
```
cd /opt/ros/humble
```

Setup environment:
```
    source /opt/ros/humble/setup.sh
```

Or add the source command to ~/.bashrc to execute it automatically when opening a terminal:
```
    gedit ~/.bashrc
```


Test
```
ros2 run demo_nodes_cpp talker

ros2 run demo_nodes_cpp listener
```
