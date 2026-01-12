# Third_vision

See With AI - MediaPipe Version
================================

See With AI is an assistive AI-powered system designed to help visually impaired individuals perceive emotions from facial expressions in real-time. By using computer vision and deep learning, the system detects human faces, extracts facial landmarks, classifies emotional states, and provides auditory feedback via text-to-speech.

Project Goals
-------------
- To create a lightweight, real-time emotion detection system using facial landmarks.
- To integrate text-to-speech (TTS) for delivering auditory feedback of the detected emotions.
- To assist people with visual impairments in understanding social cues better.
- To build an edge-friendly system using OpenCV, MediaPipe, and a trained ML model.

Core Technologies Used
-----------------------
| Technology     | Purpose                                      |
|----------------|----------------------------------------------|
| Python         | Programming language                         |
| OpenCV         | Image capture and processing                 |
| MediaPipe      | Real-time face mesh and landmark detection   |
| NumPy          | Efficient numerical operations               |
| scikit-learn / PyTorch | ML model training and prediction     |
| pyttsx3        | Offline text-to-speech (TTS) engine          |
| pickle         | Saving/loading trained ML models             |

System Workflow
----------------
1. Camera Capture:
   - A webcam captures live video frames using OpenCV.
2. Face & Landmark Detection:
   - MediaPipe's FaceMesh module detects the face and extracts 468 facial landmarks.
3. Feature Extraction:
   - The (x, y) coordinates of each landmark are flattened and normalized to form the input feature vector.
4. Emotion Classification:
   - A pre-trained machine learning model (e.g., SVM or neural network) processes the landmarks and predicts one of the seven basic emotions.
5. Auditory Feedback:
   - The predicted emotion is spoken out using pyttsx3, allowing the visually impaired user to perceive emotions audibly.

Supported Emotions
------------------
- Angry
- Disgust
- Fear
- Happy
- Sad
- Surprise
- Neutral

Project Structure
------------------
see_with_ai/
├── emotion_model.pkl         # Trained model (SVM or NN)
├── emotion_detection.py      # Main script for detection
├── tts.py                    # Text-to-speech helper module
├── requirements.txt          # Dependencies
├── README.md                 # Project description

How to Run
----------
1. Clone or download the project.
2. Ensure your environment has the required dependencies:
   pip install -r requirements.txt
3. Launch the main script:
   python emotion_detection.py
4. Press Q to exit the window.

Dataset Used
-------------
- The model was trained on a dataset consisting of facial landmarks extracted from images categorized by emotions (e.g., FER2013, AffectNet, or custom).
- Landmarks are reduced to normalized vectors for efficient inference.

Features
--------
- Real-time facial expression recognition
- Offline TTS for immediate feedback
- High-speed inference on low-power machines
- Easy to modify or upgrade with new datasets/models

Future Improvements
--------------------
- Add object detection and scene description
- Integrate with wearable devices (like smart glasses)
- Expand emotion classification using audio cues
- Multi-face support
