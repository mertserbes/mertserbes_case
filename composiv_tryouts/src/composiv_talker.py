#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10) #Inside the speaker function, it first creates a publisher object. 
    rospy.init_node('talker', anonymous=True)               #The first parameter is the topic name, the second parameter is the topic message type, 
    rate = rospy.Rate(10) # 10hz                            #and the third parameter is the amount of messages accumulated until the memory is cleared.
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
