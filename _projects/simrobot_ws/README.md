
## Create package
```
ros2 pkg create fishbot_description --build-type ament_python
```


## Create urdf
```
```


## Create luanch.py
joint_state_publisher_gui 负责发布机器人关节数据信息，通过joint_states话题发布
robot_state_publisher_node负责发布机器人模型信息robot_description，并将joint_states数据转换tf信息发布
rviz2_node 负责显示机器人的信息

Need joint_state_publisher_gui and robot_state_publisher
```
sudo apt install ros-humble-joint-state-publisher-gui ros-humble-robot-state-publisher
```


## Modify setup.py
```
from glob import glob
import os
```



## Run
```
colcon build

source install/setup.bash

ros2 launch simrobot_description display_rviz2.launch.py
```