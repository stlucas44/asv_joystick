#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from mppi_msgs.msg import BoatControl

target_topic = "force" # or /force for default settings

f_max = 10.0
f_steer = 2.0
f_turbo = 10.0
pub = []

def joy_callback(data):
    f_foreward = f_max * data.axes[1]
    f_diff = f_steer * data.axes[0]

    f_0 = f_foreward - f_diff
    f_1 = f_foreward + f_diff
    turbo = data.buttons[0]
    spin = data.buttons[2]

    if turbo == 1:
        f_0 = f_0 + f_turbo
        f_1 = f_1 + f_turbo

    if spin == 1:
        f_0 = 50
        f_1 = -50

    new_msg = BoatControl()
    new_msg.control[0] = f_0
    new_msg.control[1] = f_1


    pub.publish(new_msg)

if __name__ == '__main__':
    rospy.init_node('joystick_repeater', anonymous=True)

    rospy.Subscriber("joy", Joy, joy_callback)

    #pub = rospy.Publisher(, BoatControl, queue_size=1)
    pub = rospy.Publisher(target_topic, BoatControl, queue_size=1)

    rospy.spin()
