from mqtt_client import connect_mqtt, send_message
from config import mqtt_client
import cv2
import face_recognition as fr
import os
import numpy as np

is_cam_on = False

known_face_encodings = []
known_face_names = []

path = r'C:\Users\Afons\Documentos\OpenCV'  
for filename in os.listdir(path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img_path = os.path.join(path, filename)
        image = fr.load_image_file(img_path)
        face_encodings = fr.face_encodings(image)
        if face_encodings:
            known_face_encodings.append(face_encodings[0])
            known_face_names.append(filename.split('.')[0])  
            print(f"Rosto codificado para {filename}")
        else:
            print(f"Rosto não resconhecido {filename}")


webcam = cv2.VideoCapture(0)

while is_cam_on:

    ret, frame = webcam.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = fr.face_locations(rgb_small_frame)
    face_encodings = fr.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = fr.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = fr.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        top, right, bottom, left = face_location
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)


    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        turn_cam_off()

webcam.release()
cv2.destroyAllWindows()

# my code

def turn_cam_on():
	is_cam_on = True
	print("Camera turned on")
	send_attempt(True, "Victor")
	
def turn_cam_off():
	is_cam_on = False
	print("Camera turned off")

def send_attempt(access_granted, username=None):
	message = {
		"result": "granted" if access_granted else "denied"
	}
	
	if access_granted:
		message["username"] = username
	
	send_message(mqtt_client, "dse/register", str(message))
	print("Message sent!!")
