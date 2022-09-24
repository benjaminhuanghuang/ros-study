Installed with ROS2



```
# 记录某一个话题
ros2 bag record /sexy_girl

# 记录多个话题的数据
ros2 bag record topic-name1  topic-name2


# 记录所有话题
ros2 bag record -a


# -o name 自定义输出文件的名字
ros2 bag record -o file-name topic-name


# 录制话题数据
ros2 bag record /sexy_girl


ros2 bag info bag-file


# 播放数据
ros2 bag play xxx.db3


#-r选项可以修改播放速率，比如 -r 值，比如 -r 10,就是10倍速，十倍速播放话题
ros2 bag play rosbag2_2021_10_03-15_31_41_0.db3 -r 10

# 单曲循环
ros2 bag play rosbag2_2021_10_03-15_31_41_0.db3  -l


# 播放单个话题
ros2 bag play rosbag2_2021_10_03-15_31_41_0.db3 --topics /sexy_girl
```