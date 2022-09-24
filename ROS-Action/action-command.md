```
ros2 action list

# display action type
ros2 action list -t


ros2 interface show turtlesim/action/RotateAbsolute 



ros2 action info /turtle1/rotate_absolute 


ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.6}"
```