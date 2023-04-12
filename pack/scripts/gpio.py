import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) 
GPIO.setup(20, GPIO.OUT)
while True:
 
    GPIO.output(20, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(20,GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()    