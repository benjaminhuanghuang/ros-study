robot_localization使用`15`维向量来表示机器人的运动状态：

每3个数据一组，分别表示：
x-y-z坐标系的坐标（机器人位置）、
绕x/y/z轴的角度（机器人方向）、
沿x/y/z轴的速度、
绕x/y/z轴的角速度、
沿x/y/z轴的加速度。

robot_localization的典型用法应该是配合机器人导航模块，实现各种sensor的融合以及精确的路线导航

