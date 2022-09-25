#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class RotateWheelNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info(f"node {name} init..")
        #
        self.joint_states_publisher_ = self.create_publisher(JointState,"joint_states", 10) 
        # 
        self._init_joint_states()
        self.pub_rate = self.create_rate(30)
        self.thread_ = threading.Thread(target=self._thread_pub)
        self.thread_.start()
    
    def _init_joint_states(self):
        self.joint_speeds = [0.0,0.0]
        self.joint_states = JointState()
        self.joint_states.header.stamp = self.get_clock().now().to_msg()
        self.joint_states.header.frame_id = ""
        # 
        self.joint_states.name = ['left_wheel_joint','right_wheel_joint']
        # 
        self.joint_states.position = [0.0,0.0]
        # 
        self.joint_states.velocity = self.joint_speeds
        # 力 
        self.joint_states.effort = []

    def update_speed(self,speeds):
        self.joint_speeds = speeds

    def _thread_pub(self):
        last_update_time = time.time()
        while rclpy.ok():
            delta_time =  time.time()-last_update_time
            last_update_time = time.time()
            # 更新位置
            self.joint_states.position[0]  += delta_time*self.joint_states.velocity[0]
            self.joint_states.position[1]  += delta_time*self.joint_states.velocity[1]
            # 更新速度
            self.joint_states.velocity = self.joint_speeds
            # 更新 header
            self.joint_states.header.stamp = self.get_clock().now().to_msg()
            # 发布关节数据
            self.joint_states_publisher_.publish(self.joint_states)
            self.pub_rate.sleep()

def main(args=None):
    rclpy.init(args=args) 
    node = RotateWheelNode("rotate_fishbot_wheel")  
    node.update_speed([15.0,-15.0])
    rclpy.spin(node) 
    rclpy.shutdown() 