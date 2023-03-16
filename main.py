# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands
from chatgpt import msgresponse
from dotenv import load_dotenv
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
    
    if "!gpt" in message.content.lower():
        await message.channel.send(msgresponse(message.content[4:]))
    if "!ping" in message.content.lower():
        print(message.content)
        await message.channel.send('pong')





client.run(os.environ['DISCORD_TOKEN'])
