

```
    ros2 topic list

    ros2 topic list -t

    ros2 topic echo /<topic>

    ros2 topic info /<topic>



    ros2 interface show <mesage>


    # how fast 
    ros topic hz /topic

    # publish topic
    ros2 topic pub <mssage>
    ros2 topic pub /topic std_msgs/msg/String 'data: "123"'
    ros2 topic pub /topic std_msgs/msg/UInt32 "{data: 10}"  
```