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
    ros2 pkg create --build-type ament_cmake cpp_srvcli --dependencies rclcpp example_interfaces
```