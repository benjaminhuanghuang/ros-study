

Python build tools
```
sudo apt install python3-colcon-common-extensions
```

add to ~/.bashrc to enable the auto completion
```
source /us/share/colcon argcomplete/hook/colcon-argcomplete.bash
```

## Python project
```
mkdir app_ws
cd app_ws
mkdir src
colcon build    ## create build, install, log folders

source install/setup.bash   ## can use whatever created in this workspace
```

create a package
```
cd src
ros2 pkg create <mypy_pkg> --build-type ament_python --dependencies rclpy --node-name my_node my_py_pkg
```
