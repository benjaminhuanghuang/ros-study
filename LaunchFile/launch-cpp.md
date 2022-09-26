## launch.py
```
# 1. import
from launch import LaunchDescription
from launch_ros.actions import Node

# 2. define function generate_launch_description
def generate_launch_description():
    node = Node(
        package="demo_nodes_py",
        executable="listener"
        )
   
    # create and retrun an instance of LaunchDescription
    launch_description = LaunchDescription([node])
    return launch_description
```

## modify CMakeLists.txt to copy launch file to install folder
```
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})
```

## Modify package.xml
```
    <exec_depend>demo_nodes_cpp</exec_depend>

    <exec_depend>demo_nodes_py</exec_depend>
```


## Build
```
    cd workspace

    colcon build
```


## Run
```
    ros2 launch my_package talker.launch.py
```