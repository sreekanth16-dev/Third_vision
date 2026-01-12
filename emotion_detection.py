
import cv2
import mediapipe as mp

import numpy as np
import pickle






# MediaPipe Setup
mp_face_mesh = mp.solutions.face_mesh


# Load Emotion Classifier (pre-trained model using facial landmarks)
with open('emotion_model.pkl', 'rb') as f:
    emotion_model = pickle.load(f)  # Trained using facial landmark positions



def extract_landmark_features(landmarks):
    # Flatten and normalize landmarks (x, y) into a feature vector
    features = []
    for lm in landmarks:
        features.append(lm.x)
        features.append(lm.y)
    features = np.array(features)
    features -= np.mean(features)
    features /= np.std(features) + 1e-6
    return features.reshape(1, -1)
def detect_face(frames):

   
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=False)

    frame_rgb = cv2.cvtColor(frames, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)
   

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark
           
            features = extract_landmark_features(landmarks)
           

           

            try:
                pred = emotion_model.predict(features)
                print("Prediction:", pred)
                emotion = pred[0]
                return emotion
            except Exception as e:
                print("Emotion prediction failed:", e)
                return "unable to detect emotion"
    else:
        print("No face detected.")
        return "no face detected"


            

