

```
    sudo apt install ros-humble-usb-cam

    ros2 run usb-cam usb_cam_node_exe
```


Check the topic
```
    ros2 topic list
    ros2 topic info /image_raw

    # Bandwidth
    ros2 topic bw /image_raw


    # Print topic
    ros2 topic echo /image_raw

```