import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

audio_file = open("D:/Platzi/2025/Curso-OpenAI-API/08-TextToSpeech/speechAlloy.mp3","rb")

transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)

print("Transcripción")
print(transcript.text)