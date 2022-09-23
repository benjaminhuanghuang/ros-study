
## Install
```
    sudo apt-get -y install ament-cmake

    sudo apt instal python3-colcon-common-extensions
```


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
    ros2 pkg create <name> --dependencies rclcpp
```
defautl build-type is ament_cmake 

## Create node 
```
    cd package/src

    touch node.cpp
```
## Modify CMakeLists.txt
```
    add_executable(my_node src/wang2.cpp)
    ament_target_dependencies(my_node rclcpp)

    install(TARGETS
        my_node
        DESTINATION lib/${PROJECT_NAME}
    )
```
install path
```
install/<pkg>/lib/<pkg>
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