import time
import RPi.GPIO as GPIO
from config import BUZZER_PIN

def buzzer_beep(frequency, duration):
    p = GPIO.PWM(BUZZER_PIN, frequency)
    p.start(50)
    time.sleep(duration)
    p.stop()

def success_sound():
    buzzer_beep(1000, 0.1)
    time.sleep(0.1)
    buzzer_beep(1000, 0.1)

def failure_sound():
    buzzer_beep(500, 0.5)
