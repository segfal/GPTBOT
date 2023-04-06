import openai
from dotenv import load_dotenv
import os
import string

load_dotenv()

#get token from .env file
#openai.api_key = os.getenv("OPENAI_TOKEN")

openai.api_key = os.environ["OPENAI_TOKEN"]

def msgresponse(message):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": message
    }],
    )
    msg = response["choices"][0]["message"]["content"]
    if "As an AI language model, " in msg:
        msg = msg.replace("As an AI language model, ", "")
    if "Mongo Tom: " in msg:
        msg = msg.replace("Mongo Tom: ","")
    
    i = 0
    while msg[i] not in string.ascii_letters and i < len(msg):
        msg[i] = msg[i+1]
    if msg[0] == '"' and msg[-1] == '"':
        msg = msg[1:-1]
    msg = msg.replace("Regina George: ","Butler")
    msg = msg.split("\n\n")
    return msg
