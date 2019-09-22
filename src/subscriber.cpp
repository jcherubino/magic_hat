/*
 * subscriber is a ROS node that checks the output of the magic hat and displays * it if the quality is >= 7.
 *
 * Date last updated: 20/11/19 by Josh Cherubino
 *
 * Purpose: Help filter the output of the magic hat so that only high quality turtles are displayed
 *
 * Subscribed topic:
 * 	/magic_hat/hat_output
 */

#include "ros/ros.h"
#include "magic_hat/TurtleInfo.h"

/*callback function called when a message is published on the topic hattopic 
*this function checks if the quality of the turtle is >= to 7 and if so it is displayed 
*passes a const pointer to the callback which avoids making a copy
*/
void magicHatCallback(const magic_hat::TurtleInfo::ConstPtr& msg)
{
	if (msg->quality >= 7)
	{
		ROS_INFO("I want to show turtle [%lu] to my friend because it has quality [%u]", msg->index, msg->quality);
	}
}

//main function initialises a ros node and subscribes to /magic_hat/hat_output
int main(int argc, char **argv)
{
	ros::init(argc, argv, "subscriber");

	ros::NodeHandle n;

	ros::Subscriber sub = n.subscribe("/magic_hat/hat_output", 1000, magicHatCallback);

	//ros::spin() enters a loop which calls the callback function as messages are recieved and will exit when shutdown is called
	ros::spin();

	return 0;
}
