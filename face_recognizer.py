import cv2
import face_recognition
import numpy as np
import os
os.environ["GLOG_minloglevel"] = "3"
os.environ["MEDIAPIPE_DISABLE_LOGS"] = "1"
from tts import speak 

db_path="known_person"



def load_known_faces():
    known_faces=[]
    known_names=[]

    for file in os.listdir(db_path):
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            img=os.path.join(db_path,file)
            images=face_recognition.load_image_file(img)
            face_encodings=face_recognition.face_encodings(images)
            if face_encodings:
                known_faces.append(face_encodings[0])
                names=os.path.splitext(file)[0]
                known_names.append(names)
                
    return known_faces,known_names
    



def recognize_person(frame, known_encodings, known_names):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, faces)

    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding, tolerance=0.5)
        name = "Unknown"

        if True in matches:
            idx = matches.index(True)
            name = known_names[idx]

        names.append(name)
    if not names or all(n == "Unknown" for n in names):
        print("⚠️ Unknown person detected")
        speak("Unknown person detected")

    return names

            
def add_new_person(frame, name):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb)
    if faces:
        top, right, bottom, left = faces[0]
        face_image = frame[top:bottom, left:right]
        save_path = os.path.join(db_path, f"{name}.jpg")
        cv2.imwrite(save_path, face_image)
        speak(f"{name} has been added.")
    else:
        speak("No face detected. Please try again.")

