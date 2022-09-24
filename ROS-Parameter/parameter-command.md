

```
ros2 param list

ros2 param describe <node> <param>


ros2 param get /<node> <param>


ros2 param set /<node> <param> <value>
ros2 param set /turtlesim background_b 10



# save and load parameter
ros2 param dump /turtlesim
ros2 param laod /turtlesim ./turtlesim.yaml

ros2 run <package_name> <executable_name> --ros-args --params-file <file_name>
ros2 run turtlesim turtlesim_node --ros-args --params-file ./turtlesim.yaml

```