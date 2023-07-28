#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node) :
    def __init__(self):
        super().__init__("py_test")  # give a name to the 
        self.counter = 0
        self.get_logger().info("Hello ROS2")
        self.create_timer(1.0, self.timer_callback)


    def timer_callback(self):
        self.counter += 1
        self.get_logger().info("Timer called " + str(self.counter))


def main(args=None) :
    rclpy.init (args=args)
    node = MyNode("py_test")  # init is called
    
    rclpy.spin(node)  
    rclpy.shutdown()


if __name__ == "__main__" :
    main()
