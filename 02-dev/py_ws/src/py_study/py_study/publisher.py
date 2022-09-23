import rclpy
from rclpy.node import Node

# message type definded by ROS2
from std_msgs.msg import String


class PublisherNode(Node):
    def __init__(self,name):
        super().__init__(name)
    
        #
        #
        #
        self.pub_novel = self.create_publisher(String,"topic_sample", 10) 

        self.i = 0 
        timer_period = 3  
        self.timer = self.create_timer(timer_period, self.timer_callback)  
        

    def timer_callback(self):
        # create a message
        msg = String()
        msg.data = 'This is message %d' % self.i
        self.pub_novel.publish(msg) 
        self.get_logger().info('publish ："%s"' % msg.data)   
        self.i += 1 

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode("Tom")  
    rclpy.spin(node) 
    rclpy.shutdown() 