## launch.py

```
# 1. import
from launch import LaunchDescription
from launch_ros.actions import Node

# 2. define function generate_launch_description
def generate_launch_description():
    # create instance of launch_ros.actions.Node
    node1 = Node(
        package="village_li",
        executable="li4_node",
        parameters=[{'write_timer_period': 1}]
        )
    # create node
    node2 = Node(
        package="village_wang",
        executable="wang2_node"
        )
   
    # create and retrun an instance of LaunchDescription
    launch_description = LaunchDescription([li4_node,wang2_node])
    return launch_description
```

## modify setup.py copy launch file to install folder
```
    (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
```