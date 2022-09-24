import rclpy
from rclpy.node import Node

# message type definded by ROS2
from std_msgs.msg import String

# imort servcie defination
from my_interfaces.srv import BorrowMoney

class ServiceNode(Node):
    def __init__(self,name):
        super().__init__(name)

        # create service
        self.borrow_server = self.create_service(BorrowMoney, "borrow_money", self.borrow_money_callback)
        

    def borrow_money_callback(self,request, response):
        self.get_logger().info("request from  %s, current account is %d" % (request.name, self.account))
        
        if request.money <= int(self.account*0.1):
            response.success = True
            response.money = request.money
            self.account = self.account - request.money
            self.get_logger().info("Borrow %d, current accout is %d " % (response.money,self.account))
        else:
            response.success = False
            response.money = 0
            self.get_logger().info("Can not borrow")
        return response

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode("Tom")  
    rclpy.spin(node) 
    rclpy.shutdown() 