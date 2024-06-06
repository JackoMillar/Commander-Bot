# bot.py
import os
import discord
from discord import Intents
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("No token provided. Please check your .env file.")

print(f'Token: {TOKEN}')  # Debugging line

intents = Intents.default()  # Create a default intents instance
intents.message_content = True  # Enable the message content intent

client = discord.Client(intents=intents)  # Pass the intents to the Client

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)

# .env
DISCORD_TOKEN=MTI0ODMwMTU4MTcxMTk2NjI0OA.GZjxqY.EYl4w9AgSVmJ82fy7NojYpFLKBfGz2ul27B1L0
