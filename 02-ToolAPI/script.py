import os
from dotenv import load_dotenv
from openai import OpenAI
import requests 
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_weather(latitude:float, longitude: float) -> str:
    print("Get get_weather.. ")
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    weather_data = response.json()
    print("Resultado Funcion: ")
    print(weather_data)
    return json.dumps(weather_data)


messages = [
    {
        "role": "system",
        "content": "Eres un asistente que entrega datos sobre el clima en tiempo real usando la funcion get_weather"
    },
    {
        "role":"user",
        "content": "Cual es el clima de Bogota Colombia?"
    }
]

functions = [
     {
         "type":"function",
         "function": {
             "name": "get_weather",
             "description": "Usa esta funcion para obtener el clima",
             "parameters": {
                 "type": "object",
                 "properties":{
                     "latitude":{
                         "type": "number",
                         "description":"Latitud de la ubicacion"
                     },
                     "longitude":{
                         "type": "number",
                         "description": "Longitud de la ubicacion"

                     }
                 },
                 "required":["latitude", "longitude"]
             },
             "output":{
                 "type":"string",
                 "description":"Clima de la ubicacion pedida por el usuario"
             }

         }

     }
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=functions
    
)

assisant_message = response.choices[0].message

if assisant_message.tool_calls:
    print("Resultado primer llamnado a OpenAI")
    print(assisant_message.tool_calls)
    for tool_call in assisant_message.tool_calls:
        if tool_call.type == "function":
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            

            if function_name == "get_weather":
                print(f"El asistente esta llamando a la funcion get_weather")
                weather_info = get_weather(
                    latitude=function_args.get("latitude"),
                    longitude= function_args.get("longitude")
                )

                messages.append(assisant_message)
                messages.append({
                    "role": "tool",
                    "tool_call_id":tool_call.id,
                    "name": function_name,
                    "content": weather_info
                })

second_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages
)

finally_reply = second_response.choices[0].message.content
print("respuesta final del asistente:")
print(finally_reply)