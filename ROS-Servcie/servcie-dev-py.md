
## Server side
### Add dependency
```
<depend>my_interfaces</depend>
```

### Modify CMakeLists.txt
```
find_package(my_interfaces REQUIRED)

ament_target_dependencies(service_node 
  rclcpp 
  my_interfaces
)
```

### Include
```
#include "my_interfaces/srv/sell_novel.hpp"
```


## Client side
### Add dependency
```
<depend>my_interfaces</depend>
```

### Modify CMakeLists.txt
```
find_package(my_interfaces REQUIRED)

ament_target_dependencies(service_node 
  rclcpp 
  my_interfaces
)

add_executable(client_node src/client.cpp)
```