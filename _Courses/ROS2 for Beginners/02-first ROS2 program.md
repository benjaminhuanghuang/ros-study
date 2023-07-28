

Python build tools
```
sudo apt install python3-colcon-common-extensions
```

add to ~/.bashrc to enable the auto completion
```
source /us/share/colcon argcomplete/hook/colcon-argcomplete.bash
```

## Python project/package
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

build
```    
    cd ..
    colcon build
```

ROS2 humble need the downgrade of setuptools to  58.2.0
```
    pip3 install --upgrade setuptools==58.2.0
    pip3 list | grep setuptools
```

## C++ project/package
create a cpp package
```
    cd src
    ros2 pkg create <mycpp_pkg> --build-type ament_cmake --dependencies rclcpp --node-name my_node
```

build
```    
    cd ..
    colcon build
or
    colcon build --packages-select mycpp_pkg
```

## ROS2 Node
Subprogram in the package, responsible for only one thing. Communicate with other nodes via topics, services, actions.
### Python 
```
cd my_ws/src/my_py_pkg

touch my_first_node.py
```
run node
```
    chmod +x my_first_node.py
    ./my_first_node.py
```

install node, modify setup.py
```
entry points={
'console scripts': [
     "py_node = my_py_pkg.my_first_node:main"
    ]
}
```

run 
```
    ros2 run my_py_pkg py_node
```



### Cpp 
```
cd my_ws/src/my_py_pkg

touch my_first_node.py
```
