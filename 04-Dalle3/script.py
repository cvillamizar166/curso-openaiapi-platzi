import os
from dotenv import load_dotenv
from openai import OpenAI
import base64

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = "Crea una imagen de un desarrollador programando en python"
quality = "standard" #1024 x 1024 píxeles

response = client.images.generate(
    model = "dall-e-3",
    prompt=prompt,
    quality=quality,
    n=1
)

print(response.data[0].url)
