import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args) 
    node = Node("py_study")  # Create node
    node.get_logger().info("Hello from py_study")
    rclpy.spin(node) # Run the node and wait for ctr-c

    node.destory_node()
    rclpy.shutdown() 