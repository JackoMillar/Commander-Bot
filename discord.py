# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

client.run(TOKEN)

# .env
DISCORD_TOKEN=MTI0ODMwMTU4MTcxMTk2NjI0OA.GZjxqY.EYl4w9AgSVmJ82fy7NojYpFLKBfGz2ul27B1L0
DISCORD_GUILD=GUILD
