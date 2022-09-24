# Navigation and SLAM Using the ROS 2 Navigation Stack
https://automaticaddison.com/navigation-and-slam-using-the-ros-2-navigation-stack/

we will use information obtained from LIDAR scans to build a map of the environment and to localize on the map

The purpose of doing this is to enable our robot to navigate autonomously through both known and unknown environments(SLAM)

Two most commonly used packages for localization are the nav2_amcl package and the slam_toolbox

## Create launch file
```
cd workspace/src/basic_mobile_robot/launch

touch basic_mobile_bot_v5.launch.py
```
https://drive.google.com/file/d/1PmSJZ3HijSp1MgEQcd6m9885MSnKg1Ux/view?usp=sharing


## Add a Static Map
We now need to add a static map of our world so our robot can plan an obstacle-free path between two points. 
```
cd workspace/src/basic_mobile_robot/maps

add pgm, yaml file
```


## Add Navigation Stack Parameters
A costmap is a map made up of numerous grid cells. Each grid cell has a “cost”. The cost represents the difficulty a robot would have trying to move through that cell. 

We will use the AMCL (Adaptive Monte Carlo Localization) algorithm for localizing the robot in the world and for publishing the coordinate transform from the map to odom frame. 

```
cd workspace/src/basic_mobile_robot/params

touch nav2_params.yaml
```

Create an RViz Configuration File


Update the Plugin Parameters int model.sdf


Update the Robot Localization Parameters in config/ekf.yaml

