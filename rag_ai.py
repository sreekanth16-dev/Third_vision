import os
import google.generativeai as genai
from sentence_transformers import SentenceTransformer, util

# Set your Gemini API key
genai.configure(api_key="AIzaSyDGRwgaftZH6-T9kd8UT2KmFUBnYi_SI1E")



 
model = genai.GenerativeModel(model_name="gemini-2.0-pro-exp")

config=genai.GenerationConfig(temperature=0.7,max_output_tokens=100)





def generate_response(query):
   
    prompt = f"""
You are a helpful, intelligent chatbot that can answer general questions with clear and useful explanations.

User: {query}
Answer:
"""
    response = model.generate_content(prompt)
    return response.text.strip()


