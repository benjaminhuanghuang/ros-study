Used to fake the joint states


This tool will look at the robot description that's published by robot_state_publisher and scan through the urdf and find any joins that could be moved. 

It will display a slider for them and publish the value of the slider as a joint states.

```
    ros2 run joint_state_publisher_gui joint_state_publisher_gui
```

