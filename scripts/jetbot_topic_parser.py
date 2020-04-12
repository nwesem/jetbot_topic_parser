#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from jetbot_ros.msg import Float32Array


class JetbotParser:
    def __init__(self):
        self.pub = rospy.Publisher('/jetbot_motors/cmd_raw', Float32Array, queue_size=1)
        self.sub = rospy.Subscriber("/joy", Joy, self.callback, queue_size=1)
        rospy.init_node("JetbotParser", anonymous=True)

    def callback(self, data):
        rospy.loginfo("speed- = [%f, %f]" % (data.axes[1], data.axes[4]))
        msg = Float32Array()
        msg.data = [data.axes[1], data.axes[4]]
        self.pub.publish(msg)

    def listen(self):
        rospy.spin()


def main():
    parser = JetbotParser()
    parser.listen()


if __name__ == '__main__':
    main()

