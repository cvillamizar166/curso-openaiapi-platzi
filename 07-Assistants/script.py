import os
from dotenv import load_dotenv
from openai import OpenAI
import time

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

assintant_id= 'asst_HAVWLu8ohLWgDv4c1JP4Bf1G'
#crear hilo
thread = client.beta.threads.create()
#open AI almacenaria las conversaciones
print(f"Hilo creado con id {thread.id}")

#Crea el mensaje y lo agrega al hilo
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Cuanto es 16284+991893-771939*12456? Puedes ejecutar código para esto"
)

#Obtiene el hilo y lo comienza a ejecutar
print("Ejecutando el asistente")
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assintant_id
)

#se verifica hasta que el run se complete
while True:
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    if run.status == "completed":
        print("se completo la respuesta")
        break

    time.sleep(1)

#Una vez completado, listamos los mensajes para ver el codigo que genero el asistente
if run.status == "completed":
    run_steps = client.beta.threads.runs.steps.list(
        thread_id=thread.id,
        run_id=run.id
    )

    #mostrar las llamadas a la herramienta que tiene el codigo que se ejecuta
    for step in run_steps:
        #print("steps")
        #print(step)
        if step.step_details.type == "tool_calls":
            for tool_call in step.step_details.tool_calls:

                if tool_call.type == "code_interpreter":
                    print("Código Python")
                    print(tool_call.code_interpreter.input)

    #lista los mensajes 
    messages = client.beta.threads.messages.list(
        thread_id=thread.id,
        order="desc",
        limit=3
    )

    for msg in messages:
        #print("mensajes")
        #print(msg)
        if msg.role == "assistant":
            for content_block in msg.content:
                print(content_block.text.value)