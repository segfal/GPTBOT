# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands
from chatgpt import msgresponse
from dotenv import load_dotenv
import time
import random
load_dotenv()
client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


#using a command to get the bot to respond
@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return
    #new user join
    if message.content.startswith('!hello'):
        
        #hello with user name
        await message.channel.send(f'Hello <@{message.author.id}>!')
    if "!jerb" in message.content.lower():
        await message.channel.send(random.choice([
            "Leave me alone, I'm trying to sleep.",
            "who are you?",
            "tf do you want?",
            "I'm not your bitch",
            "Stop it"
        ]))
        return None
    
    if "!gpt" in message.content.lower():
        x = msgresponse(message.content[4:])
        ##add user name in first line
        x[0] = f"<@{message.author.id}> {x[0]}"
        for i in x:
            async with message.channel.typing():
                time.sleep(random.randint(1,7))
            await message.channel.send(i+"\n\n")
        #await message.channel.send(msgresponse(message.content[4:]))
    if "!ping" in message.content.lower():
        print(message.content)
        await message.channel.send('pong')
    




client.run(os.getenv('DISCORD_TOKEN'))
#client.run(os.environ['DISCORD_TOKEN'])
