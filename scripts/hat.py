#!/usr/bin/env python

from random import randint 
import rospy
from magic_hat.msg import TurtleInfo

def magic_hat():
    '''function to create a ros publisher to pull turtles out of the magic hat a
    at a rate of 5 hz with a random quality level between 1 to 10 and an index.'''
    pub = rospy.Publisher('hattopic', TurtleInfo, queue_size=10)
    rospy.init_node('magichat', anonymous=True)
    rate = rospy.Rate(5) #hz
    #initialise counter variable for use msg.index
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

