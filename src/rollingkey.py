#! /usr/bin/env python3
# 쉘빙 설정 

import rospy
from std_msgs.msg import Float64
    # pub /left_arm_controller/command std_msgs/Float64 "data: 0.0"

def main():
    rospy.init_node('rollingarm')
    # 노드 이름 설정
    left_arm_pub = rospy.Publisher('left_arm_controller/command' ,Float64,queue_size=10)
    right_arm_pub = rospy.Publisher('right_arm_controller/command' ,Float64,queue_size=10)    
    # 퍼블리셔 설정 어디에 보낼건지,데이터타입,큐사이즈

    # left_direction = 0.0
    while not rospy.is_shutdown():
        key = input("w or x or s or e or q: ")

        if key == 'w':
            right_arm_pub.publish(-1.0)
            left_arm_pub.publish(-1.0)
            rospy.sleep(0.01)
        elif key == 'x':
            right_arm_pub.publish(1.0)
            left_arm_pub.publish(1.0)
            rospy.sleep(0.01)
        elif key == 's':
            right_arm_pub.publish(0.0)
            left_arm_pub.publish(0.0)
            rospy.sleep(0.01)
        elif key == 'e':
            right_arm_pub.publish(-1.0)
            left_arm_pub.publish(1.0)
            rospy.sleep(0.01)
        elif key == 'q':
            break
    # 방향과 보낼 메세지 설정
        


    pass

if __name__ =='__main__':

    main()
    pass