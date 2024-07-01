import RPi.GPIO as GPIO

BUZZER_PIN = 17
TRIG_PIN = 23
ECHO_PIN = 24
SERVO_PIN = 22

pwm = None 
mqtt_client = None

def setup_gpio():
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    pwm = GPIO.PWM(SERVO_PIN, 50)
    pwm.start(0)

def get_pwm():
    global pwm
    return pwm

def cleanup_gpio():
    GPIO.cleanup()
