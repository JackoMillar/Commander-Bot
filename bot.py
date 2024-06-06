# bot.py
import os
import discord
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()  # Load the .env file
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()  # Create a default intents instance
intents.message_content = True  # Enable the message content intent

bot = commands.Bot(command_prefix='/', intents=intents)  # Use commands.Bot

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='result')
async def result(ctx, winning_pair: str, *losing_pairs: str):
    # Split the winning pair into player and commander
    winning_player, winning_commander = winning_pair.strip('[]').split(', ')

    # Print the winning pair
    print(f"Winning player: {winning_player}")
    print(f"Winning commander: {winning_commander}")

    # Process and print each losing pair
    for pair in losing_pairs:
        losing_player, losing_commander = pair.strip('[]').split(', ')
        print(f"Losing player: {losing_player}")
        print(f"Winning commander against: {losing_commander}")

    # Respond in Discord
    response = f"Winner: {winning_player} with {winning_commander}\n"
    response += "Losers:\n"
    for pair in losing_pairs:
        losing_player, losing_commander = pair.strip('[]').split(', ')
        response += f"{losing_player} (Commander: {losing_commander})\n"

    await ctx.send(response)


bot.run(TOKEN)