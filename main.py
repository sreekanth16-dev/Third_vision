# visually_impaired_assistant/

# -------------------------
# main.py (Auto Assistant)
# -------------------------
import cv2
import time
from detect_object import detect_objects
from read_text import read_and_display_text
from caption import caption_image
from tts import speak
from voice_command import listen_for_command, get_intent
from face_recognizer import recognize_person, add_new_person, load_known_faces
from emotion_detection import detect_face
from rag_ai import generate_response

cap = cv2.VideoCapture(0)
MODE_DURATION = 7
MODES = ['auto']  
known_encodings, known_names = load_known_faces()

print("\n AI Assistant for Visually Impaired - Started")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
 
        query = listen_for_command()
        intent ="person"
        print(intent)
        

        if intent == "person":
            names = recognize_person(frame, known_encodings, known_names)
            speak("I see " + ", ".join(names) if names else "I don't recognize anyone.")

            emotion = detect_face(frame)
            print("Detected emotion:", emotion)  # <-- ADD THIS
            speak(f"The {names if names else 'person'} looks {emotion}.")

        elif intent == "object":
            items = detect_objects(frame)
            captions=caption_image(frame)
            speak(captions)
            speak("I see: " + ", ".join(items) if items else "I don't see any objects.")


        elif intent == "text":
            text = read_and_display_text(frame)
            speak(text)
            speak("It says: " + text if text else "I can't read any text.")

       

        elif intent=="remember":
            import re
            match = re.search(r"remember this person as (\w+)", query)
            if match:
                name = match.group(1).capitalize()
                add_new_person(frame, name)
                known_encodings, known_names = load_known_faces()
                speak(f"Okay, I’ve remembered {name}.")
        elif intent=="no":
            speak("no voice detected")


        else:
            response = generate_response(query)
            speak(response)

        time.sleep(3)

except KeyboardInterrupt:
    print("\n Stopped by user")

cap.release()
cv2.destroyAllWindows()