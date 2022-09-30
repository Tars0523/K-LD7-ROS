#!/usr/bin/env python
#-*- coding:utf-8 -*-
import rospy
from radar.msg import radar_message

def RadarDataStore(data):
    # 받은 내용(data)를 터미널에 출력
    rospy.loginfo("------")
    rospy.loginfo("Start Time(sec): %d", data.start_time.secs)
    rospy.loginfo("Max speed: %f", data.num)

def main():
    rospy.init_node('RadarDataStore', anonymous=False)
    rospy.Subscriber("radar_data", radar_message, RadarDataStore)
    rospy.spin()

if __name__ == '__main__':
    main()
