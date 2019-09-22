#!/usr/bin/env python

'''hat.py is a ROS node that publishes the output of a 'magic hat' that contains an infinite amount of turtles with an index and a quality.

Date Last Updated: 22/9/19 by Josh Cherubino

Purpose: Publish the output of the magic hat so that the corresponding subscriber node can determine whether to display the turtles

Subscribed topic/s:

Published topics/s:
    /magic_hat/hat_output

'''

from random import randint 
import rospy
from magic_hat.msg import TurtleInfo

def magic_hat():
    '''function to create a ros publisher to pull turtles out of the magic hat a
    at a rate of 5 hz with a random quality level between 1 to 10 and an index.'''
    pub = rospy.Publisher('/magic_hat/hat_output', TurtleInfo, queue_size=10)
    rospy.init_node('magic_hat', anonymous=True)
    rate = rospy.Rate(5) #hz
    #initialise counter variable for use in msg.index
    counter = 0
    msg = TurtleInfo()
    while not rospy.is_shutdown():
        msg.quality = randint(1, 10)
        msg.index = counter
        rospy.loginfo(msg)
        pub.publish(msg)
        counter += 1
        rate.sleep()

if __name__ == "__main__":
    try:
        magic_hat()
    except rospy.ROSInterruptException:
        pass

