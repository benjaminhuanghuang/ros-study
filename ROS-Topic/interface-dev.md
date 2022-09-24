## create package
```
    ros2 pkg create my_interface
```


## Create msg
```
    cd <node>
    mkdif msg
    cd msg
    touch <name>.msg
```


## Modify CMakelists.txt
```
# Novel.msg use sensor_msgs
find_package(sensor_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Novel.msg"
   DEPENDENCIES sensor_msgs
 )
```

## Add dependencies in package.xml
```
<depend>sensor_msgs</depend>
<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```


## Show message detail
```
ros2 interface package <package>

ros2 interface show std_msgs/msg/String

ros2 interface proto my_interface/msg/Novel2
```