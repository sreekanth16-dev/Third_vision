from ultralytics import YOLO
import cv2



model=YOLO("yolov8n.pt")

def detect_objects(frame):
    result=model.predict(source=frame,conf=0.7,verbose=False)
    names=result[0].names
    objects=[names[int(cls)] for cls in result[0].boxes.cls]
    return list(set(objects))

