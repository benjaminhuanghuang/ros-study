# URDF (Unified Robot Description format)

1. Create package
```
    ros2 pkg create box
```


2. Create urdf


3. Create launch

How to Load a URDF File into Gazebo – ROS 2
https://automaticaddison.com/how-to-load-a-urdf-file-into-gazebo-ros-2/



4. Modify CMakeLists.txt
```
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)
```