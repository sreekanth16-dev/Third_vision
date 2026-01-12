# import pytesseract
# import cv2
# pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# def read_text(frame):
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     result = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    
#     texts = [result['text'][i] for i in range(len(result['text'])) if result['text'][i].strip() != '']
#     return " ".join(texts)

import cv2
import pytesseract
from tts import speak
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def read_and_display_text(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Get OCR data with bounding boxes
    data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

    extracted_text = []
    n_boxes = len(data['text'])

    for i in range(n_boxes):
        text = data['text'][i].strip()
        conf = int(data['conf'][i])

        # Filter out weak results
        if text != "" and conf > 60:
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            extracted_text.append(text)

    detected_text= " ".join(extracted_text)
    return detected_text







   

   
