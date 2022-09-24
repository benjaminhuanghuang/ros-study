import rclpy
from rclpy.node import Node

class Talk(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("Hello, I'm %s" % name)


def main(args=None):
    rclpy.init(args=args)
    node = Talk("Tom")  
    rclpy.spin(node) 
    rclpy.shutdown() 