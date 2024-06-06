# bot.py
import os
import re
import discord
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
async def result(ctx, *, arg: str):
    # Use regex to extract the pairs from the input string
    pattern = re.compile(r'\[(.*?)\]')
    matches = pattern.findall(arg)

    if not matches or len(matches) < 2:
        await ctx.send("Invalid input format. Please use: /result [Winning player, Winning Commander] [Losing player 1, Winning commander 1] [Losing player 2, Winning commander 2] [Losing player 3, Winning commander 3]")
        return

    # Extract the winning pair
    winning_pair = matches[0]
    winning_player, winning_commander = map(str.strip, winning_pair.split(','))

    # Print the winning pair
    print(f"Winning player: {winning_player}")
    print(f"Winning commander: {winning_commander}")

    # Prepare the response message
    response = f"**Winner:**\n{winning_player} with {winning_commander}\n**Losers:**\n"

    # Process and print each losing pair
    for pair in matches[1:]:
        losing_player, losing_commander = map(str.strip, pair.split(','))
        print(f"Losing player: {losing_player}")
        print(f"Losing commander: {losing_commander}")
        response += f"{losing_player} with {losing_commander}\n"

    # Respond in Discord
    await ctx.send(response)

bot.run(TOKEN)
