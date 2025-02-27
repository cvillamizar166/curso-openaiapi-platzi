import os
from dotenv import load_dotenv
from openai import OpenAI
import base64

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def enconde_image_to_base64(path):
    with open(path,"rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    

#Podemos enviarle la Url si la tenemos o en caso contrario en base64 
messages = [
    {
        "role": "system",
        "content": "Eres un asistente que analiza las imagenes a gran detalle."
    },
    {
        "role":"user",
        "content":[
            {
                "type": "text",
                "text": "Hola puedes analizar esta imagen?"
            },
            {
                "type":"image_url",
                "image_url":{
                    #"url": f"data:image/png;base64,{enconde_image_to_base64('D:/Platzi/2025/Curso-OpenAI-API/03-Images/imagenes/plt.png')}"
                    "url": f"data:image/jpg;base64,{enconde_image_to_base64('D:/Platzi/2025/Curso-OpenAI-API/03-Images/imagenes/city.jpg')}"
                }
            }
        ]
    }
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

print("Respuesta del analisis de la imagen")
print(response.choices[0].message.content)