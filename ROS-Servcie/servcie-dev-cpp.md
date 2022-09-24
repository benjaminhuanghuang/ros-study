## create package
```
    ros2 pkg create my_interface
```


## Create msg
```
    cd <node>
    mkdir srv
    cd srv
    touch <name>.srv
```


## Modify CMakelists.txt
```
# Novel.msg use sensor_msgs
find_package(sensor_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
   "srv/BorrowMoney.srv"
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
ros2 interface package my_interface

ros2 interface show my_interface/srv/BorrowMoney

ros2 interface proto my_interface/msg/Novel2


ros2 interface show my_interface/srv/SellNovel

ros2 interface proto my_interface/srv/SellNovel 
```


## Create service code
### Add dependency
```
<depend>my_interfaces</depend>
```

### Import service defination 
```
from my_interfaces.srv import BorrowMoney
```