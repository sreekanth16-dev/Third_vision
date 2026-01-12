from transformers import BlipProcessor,BlipForConditionalGeneration
from PIL import Image
import torch


processor=BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=True)
model=BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-base')
  


def caption_image(frame):
    try:
        image = Image.fromarray(frame)
        inputs = processor(images=image, return_tensors="pt")
        out = model.generate(**inputs)
        return processor.decode(out[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error generating caption: {e}"