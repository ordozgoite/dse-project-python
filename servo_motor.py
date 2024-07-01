import time
import RPi.GPIO as GPIO
from config import SERVO_PIN, get_pwm
from buzzer import success_sound

def set_angle(angle):
    pwm = get_pwm()
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

def open_door():
    print("open_door")
    success_sound()
    set_angle(90)
    time.sleep(5)
    close_door()

def close_door():
    print("close_door")
    set_angle(0)
