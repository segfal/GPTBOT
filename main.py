# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands
from chatgpt import msgresponse
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


#using a command to get the bot to respond
@client.event
async def on_message(message):
    if message.content.startswith('!GPT'):
        await message.channel.send(msgresponse(message.content[4:]))




client.run(os.environ["DISCORD_TOKEN"])
