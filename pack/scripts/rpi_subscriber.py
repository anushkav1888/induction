#!/usr/bin/env python3
import rospy
from roboclaw_3 import Roboclaw
from std_msgs.msg import String
import signal
import time
import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) 
GPIO.setup(20, GPIO.OUT)


def SignalHandler_SIGINT(SignalNumber,Frame):
    roboclaw_drive.ForwardM1(0x80,0)
    roboclaw_drive.BackwardM2(0x80,0) 
    sys.exit(0)

signal.signal(signal.SIGINT,SignalHandler_SIGINT) 


def callback(direction):
   rospy.loginfo(f"heard '{direction.data}'")
   if direction.data=='Forward':
    print("forward")
    roboclaw_drive.ForwardM2(0x80,15)
    roboclaw_drive.BackwardM1(0x80,15)
   elif direction.data=='Backward':
    print("backward")
    roboclaw_drive.ForwardM1(0x80,15)
    roboclaw_drive.BackwardM2(0x80,15) 
   elif direction.data=='Right':
    print("right")
    roboclaw_drive.BackwardM2(0x80,15)
    roboclaw_drive.BackwardM1(0x80,15)
   elif direction.data=='Left':
    print("left")
    roboclaw_drive.ForwardM1(0x80,15)
    roboclaw_drive.ForwardM2(0x80,15)
   elif direction.data=="Stop":
    print("Stop")
    roboclaw_drive.ForwardM1(0x80,0)
    roboclaw_drive.BackwardM2(0x80,0) 
   elif direction.data=="Blink":
    for i in [0,1]:
 
        GPIO.output(20, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(20,GPIO.LOW)
        time.sleep(1)
GPIO.cleanup() 
   
def listener():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("drive-directives", String, callback) 
    rospy.spin()

if __name__=='__main__':
   
       roboclaw_drive=Roboclaw('/dev/drive',9600)

    
     
         
      
       roboclaw_drive.Open()
       listener()
       