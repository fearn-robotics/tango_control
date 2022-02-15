#include "ros/ros.h"
#include "std_msgs/Int8.h"
#include "tango_msgs/relays.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

tango_msgs::relays motor_msg;
tango_msgs::relays infrared_msg;
tango_msgs::relays lidar_msg;


int main(int argc, char **argv) {
    ros::init(argc, argv, "safety_relays");
    ros::NodeHandle n;
    ros::Rate loop_rate(1);   
    ros::Publisher mc_pub = n.advertise<tango_msgs::relays>("/tango_msgs/relays", 1);
    int count = 0;

    while(ros::ok()) {
        if (count < 10) {
            motor_msg.number = 1;
            motor_msg.state = 1;
            mc_pub.publish(motor_msg);
            std::cout << "message sent"  << std::endl;
ros::spinOnce();
        loop_rate.sleep();
        
            infrared_msg.number = 3;
            infrared_msg.state = 1;
            mc_pub.publish(infrared_msg);
            std::cout << "message sent"  << std::endl;
ros::spinOnce();
        loop_rate.sleep();
        
            lidar_msg.number = 5;
            lidar_msg.state = 1;
            mc_pub.publish(lidar_msg);
            std::cout << "message sent"  << std::endl;
        }
        ros::spinOnce();
        loop_rate.sleep();
        count++;
    }

    if (ros::isShuttingDown() ) {
        /*relay_msg.number = 1;
        relay_msg.state = 0;
        mc_pub.publish(relay_msg);
        std::cout << "message 2 sent"  << std::endl;*/
    }

    return 0;
}
