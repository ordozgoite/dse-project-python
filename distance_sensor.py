import time
import RPi.GPIO as GPIO
from config import TRIG_PIN, ECHO_PIN

def track_distance():
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.1)
    
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    
    GPIO.output(TRIG_PIN, False)
    
    while GPIO.input(ECHO_PIN) == 0:
        start_pulse = time.time()
    
    while GPIO.input(ECHO_PIN) == 1:
        end_pulse = time.time()
        
    pulse_duration = end_pulse - start_pulse
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance
