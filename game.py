import random, sys
from copy import deepcopy
import discord
# from database_handler import RPGDatabase

# db = RPGDatabase()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # Get the server (guild)
    guild = discord.utils.get(client.guilds, name='Game Test Server')

    # Get the channel where you want to send the message
    channel = discord.utils.get(guild.text_channels, name='general')

    # Send the message
    await channel.send("I'm now online!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Bye!')

client.run('MTE0NTc5NzQ3ODQwNzQ3MTIyNg.GzlS1j.uuZx0iCd8-G9jj6LMuOVoJbn81L3yx9ib1HKk8')
