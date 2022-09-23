
## source ROS2 environment
```
source /opt/ros/humble/setup.bash
```

## create directory for workspace
```
    mkdir -p ~/<workspace>/src
    cd ~/<workspace>/src
```
## Create packages under <workspace>/src
```
    ros2 pkg create <name> --build-type ament_python --dependencies rclpy
```

## Create node 

## Modify setup.py
```
    entry_points={
        'console_scripts': [
            "my_node = <pkg>.<node>:main"
        ],
    },
```

## Resolve dependencies

From root of workspace, run the command
```
    rosdep install -i --from-path src --rosdistro humble -y
```

## Build the workspace with colcon

From the root of workspace, run the command
```
    colcon build
```
## Run node
```
    . install/setup.sh
    
    ros2 run <pkg> <node>

    ros2 node list
```