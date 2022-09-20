# Writing a simple publisher and subscriber (Python)
http://docs.ros.org.ros.informatik.uni-freiburg.de/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html


1. create workspace

2. create package
navigate into ros2_ws/src, and run the package creation command:
```
ros2 pkg create --build-type ament_python py_pubsub
```

3. Write the publisher node

```

```




## Build and run

check for missing dependencies before building (in the root of your workspace)
```
    rosdep install -i --from-path src --rosdistro humble -y
```

build your new package (in the root of your workspace)
```
    # install colcon
    sudo apt install python3-colcon-common-extensions

    colcon build --packages-select py_gpspub
```


## Run
```
    ros2 run <package> <entry_point>

For example:
    ros2 run py_gpspub talker
```