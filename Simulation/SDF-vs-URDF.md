SFD 是Gazebo的原生格式

URDF是ROS的原生支持格式，但在某些情况下（尤其是Gazebo仿真时），使用SDF格式会更加合理

Rviz可视化只能使用URDF，机器人的Gazebo仿真只能使用SDF

urdf use decribes the a robot, sdf describe the world taht is being simulated.


Gazebo官方还提供 urdf转sdf 命令
```
gz sdf -p my_model.urdf > my_model.sdf
```


SDF 转 URDF
https://link.zhihu.com/?target=https%3A//github.com/andreasBihlmaier/pysdf

```
rosrun pysdf sdf2urdf.py model.sdf model.urdf
```