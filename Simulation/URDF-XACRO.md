# URDF

A URDF (Universal Robot Description Format) file is an XML file that describes what a robot should look like in real life

URDF是ROS的原生支持格式

Rviz可视化只能使用URDF，

The body of a robot consists of two components:
- Links are connected to each other by joints.
- Joints are the pieces of the robot that move, enabling motion between connected links.

robotic arm is made of rigid pieces (links) and non-rigid pieces (joints).
Servo motors at the joints cause the links of a robotic arm to move.


http://wiki.ros.org/urdf/Tutorials