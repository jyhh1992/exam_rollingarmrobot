#! /usr/bin/env python3
# 쉘빙 설정 

import rospy
from std_msgs.msg import Float64
    # pub /left_arm_controller/command std_msgs/Float64 "data: 0.0"

def main():
    rospy.init_node('rollingarm')
    # 노드 이름 설정
    left_arm_pub = rospy.Publisher('left_arm_controller/command' ,Float64,queue_size=10)
    # 퍼블리셔 설정 어디에 보낼건지,데이터타입,큐사이즈

    # left_direction = 0.0
    while not rospy.is_shutdown():
        left_direction = float(input("-1.0~1.0:"))
        left_arm_pub.publish(left_direction)
    # 방향과 보낼 메세지 설정
        rospy.sleep(0.01)


    pass

if __name__ =='__main__':

    main()
    pass