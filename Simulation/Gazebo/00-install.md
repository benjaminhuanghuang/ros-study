https://classic.gazebosim.org/tutorials?tut=install_ubuntu


Install
```
curl -sSL http://get.gazebosim.org | sh

or

sudo apt install ros-humble-gazebo-*
```

Run
```
gazebo

or

ros2 launch gazebo_ros gazebo.launch.py
```

Check Gazebo version

```
dpkg -l | grep gazebo
```