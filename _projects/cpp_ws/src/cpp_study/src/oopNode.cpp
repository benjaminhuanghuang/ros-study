
#include "rclcpp/rclcpp.hpp"

class DogNode : public rclcpp::Node
{

public:
    DogNode(std::string name) : Node(name)
    {
        RCLCPP_INFO(this->get_logger(), "Hello, I'm %s.", name.c_str());
    }

private:
   
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<DogNode>("Tom");
   
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}