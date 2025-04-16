#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraNode:
    def __init__(self):
        rospy.init_node('camera_node', anonymous=True)
        self.image_pub = rospy.Publisher('camera/image_raw', Image, queue_size=10)
        self.bridge = CvBridge()
        self.camera_id = rospy.get_param('~camera_id', 0)
        self.camera = cv2.VideoCapture(self.camera_id)
        self.rate = rospy.Rate(30)  # 30Hz
        
    def run(self):
        while not rospy.is_shutdown():
            ret, frame = self.camera.read()
            if ret:
                try:
                    # Convert OpenCV image to ROS image message
                    img_msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
                    self.image_pub.publish(img_msg)
                except Exception as e:
                    rospy.logerr(f"Error converting image: {e}")
            self.rate.sleep()

if __name__ == '__main__':
    try:
        node = CameraNode()
        node.run()
    except rospy.ROSInterruptException:
        pass 