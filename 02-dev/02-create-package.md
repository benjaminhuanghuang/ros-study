# 
https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html


## Create package Python
```
```

## Create package c++
Install ament-cmake
```
sudo apt-get -y install ament-cmake
```

Create package
```
    ros2 pkg create <package> --build-type {ament_cmake, cmake, ament_python} --dependencies rclcpp example_interfaces

    ros2 pkg create <package> --build-type ament_cmake cpp_srvcli --dependencies rclcpp example_interfaces
```
ament_cmake is the default build type

