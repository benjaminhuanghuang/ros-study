# URDF

A URDF (Universal Robot Description Format) file is an `XML` file that describes what a robot should look like in real life

URDF使用XML格式描述机器人文件

URDF是ROS的原生支持格式

Rviz可视化只能使用URDF，

URDF由两种关键组件共同组成

The body of a robot consists of two components:
- Links are connected to each other by joints.
- Joints are the pieces of the robot that move, enabling motion between connected links.

robotic arm is made of rigid pieces (links) and non-rigid pieces (joints).
Servo motors at the joints cause the links of a robotic arm to move.

```
<?xml version="1.0" ?>

<robot name="my_robot">
    <link name="arm_link">
        <visual>
            <geometry> 
            <origin>
            <material>
        </visual>
        
        <collision>
            <geometry> 
            <origin>
        </collision>

        <inertial>
            <mass>
            <origin>
            <inertia>
        </inertial>   
    </link>

    <joint name="inertial_joint" type="fixed">
        <parnet link="">
        
        <chind link="">

        <origin xyz="" rpy="">

        <axis xyx="">

        <limit lower="" upper="" velocity="" offort="">
    </joint>
</robot>
```

http://wiki.ros.org/urdf/Tutorials


## Joint Types
- Revolution (has limit): arm
- Continuous (no limit): wheel
- Prismatic
- Fixed




