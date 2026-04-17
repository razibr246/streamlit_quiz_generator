import google.generativeai as genai
from dotenv import load_dotenv
import os, io
from gtts import gTTS

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def note_generator(images):
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = "Summarize the picture in note format in Bangla at max 100 words. Add markdown to differentiate sections."
    response = model.generate_content([images, prompt])
    return response.text

def audio_transcription(text):
    speech = gTTS(text, lang='bn', slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(image, difficulty):
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"Generate 3 quizzes based on the {difficulty}. Add markdown for options. Add correct answer after quiz."
    response = model.generate_content([image, prompt])
    return response.text
