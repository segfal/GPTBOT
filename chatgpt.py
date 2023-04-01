import openai
from dotenv import load_dotenv
import os


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
    msg = msg.split("\n\n")
    return msg
