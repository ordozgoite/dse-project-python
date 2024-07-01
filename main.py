import time
from config import BUZZER_PIN, TRIG_PIN, ECHO_PIN, SERVO_PIN, setup_gpio, cleanup_gpio, mqtt_client
from distance_sensor import track_distance
from servo_motor import open_door, close_door
from buzzer import success_sound, failure_sound
from mqtt_client import connect_mqtt, send_message
from webcam import turn_cam_off, turn_cam_on

min_distance = 10
inactivity_delay_sec = 5 # tempo necessário pra que a câmera desligue após o instante em que nenhuma rosto é detectado

def main_loop():
    while True:
        distance = track_distance()
        print(f"Distance: {distance}cm")
        
        if distance < min_distance:
            turn_cam_on()

if __name__ == "__main__":
    setup_gpio()
    mqtt_client = connect_mqtt()
    try:
        main_loop()
    except KeyboardInterrupt:
        print("Exiting program")
    finally:
        cleanup_gpio()
