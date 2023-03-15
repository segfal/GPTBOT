import openai
import os






openai.api_key = os.environ["OPENAI_TOKEN"]
'''
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": "Recipe for a chocolate cake"
    }],
)
'''
def msgresponse(message):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
        "role": "user",
        "content": message
    }],
    )

    return response["choices"][0]["message"]["content"]

#print(response["choices"][0]["message"]["content"])
