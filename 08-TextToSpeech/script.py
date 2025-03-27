import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_text_to_speech(text:str,output_file="speechAlloy.mp3"):
    """
    Genera un archivo de audio a partir de un texto utilizando la API de OpenAI.
    El metodo with_streaming_response. Nos permite obtener el audio en tiempo real,
    es decir reproducirse antes de que se genere y esté disponible el archivo completo.

    Speech.create
    Obtendria el audio una vez este disponible el archivo

    Args:
        text (str): El texto que se convertirá a voz.
        output_file (str): El nombre del archivo de salida (por defecto "speechAlloy.mp3").

    """
    #with con Create espera hasta que toda la respuesta se haya recibido 
    #antes de continuar con el siguiente paso (es decir, el archivo se guarda sólo cuando toda 
    # la conversión de texto a voz se ha completado)
    with client.audio.speech.with_streaming_response.create(
        model='tts-1',
        voice='alloy',
        input=text
    ) as response:
        response.stream_to_file(output_file)

if __name__ == "__main__":
    text="Hola cada dia hay mas avances en OpenAI. Colombia"
    output_file="speechAlloy.mp3"
    generate_text_to_speech(text,output_file)