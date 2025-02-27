import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#messages contienen el contenido y el rol
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"system",
            "content": "Te llamas PlatziVisionCarl, presentate como tal"
        },
        {
            "role": "user",
            "content": "Hola, ¿Cómo estás?"
        },
        {
            "role":"assistant",
            "content": "Hola soy PlatziVisionCarl, un asistente virtual listo para ayudarte. ¿En qué puedo asistirte hoy?"
        },
        {
            "role":"user",
            "content":"¿Qué es PlatziVisionCarl?"
        }

    ],
    max_tokens=100,
    temperature=0.9
)

#obtener respuesta
print(response.choices[0].message.content)