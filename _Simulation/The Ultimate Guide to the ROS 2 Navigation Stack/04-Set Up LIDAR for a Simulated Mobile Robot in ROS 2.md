# Set Up LIDAR for a Simulated Mobile Robot in ROS 2
https://automaticaddison.com/set-up-lidar-for-a-simulated-mobile-robot-in-ros-2/


## Add lider_link into SDF
```
<link name="lidar_link">    
```

## Test SDF
Add the following line to the bottom of the bashrc file:
```
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/ben/workspace/slam_ws/src/basic_mobile_robot/models/
```

open gazebo
On the left-hand side, click the `Insert` tab.

On the left panel, find your robot. 

see the output of the /scan topic, you type:
```
ros2 topic echo /scan
```


## Add lider into URDF file
https://drive.google.com/file/d/168iIcJMdpRvXKeMPy5UHsCB_ICuWlCjG/view?usp=sharing

## Modify launch file
https://drive.google.com/file/d/1bhjBqEgXEYhzGED8wm0oeW2kn43hsSTP/view?usp=sharing