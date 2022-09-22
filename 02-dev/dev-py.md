
1. source ROS2 environment
```
source /opt/ros/humble/setup.bash
```

2. create directory
```
mkdir -p ~/<workspace>/src
cd ~/<workspace>/src
```

3. Create packages under <workspace>/src


4. Resolve dependencies
Go to root of workspace, run the command
```
    rosdep install -i --from-path src --rosdistro humble -y
```

5. Build the workspace with colcon
From the root of workspace, run the command
```
    colcon build
```