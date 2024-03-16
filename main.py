import discord
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
from utils import get_fe, get_fone

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Online')
    background_task.start()

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        channel = bot.get_channel(int(CHANNEL_ID))
        print(channel)

        prefix = "7" 
        if channel: 
            command = message.content[len(prefix):]  # Get the command
            print(command)

@tasks.loop(hours=24)
async def background_task():
    print('Background task started')
    await bot.wait_until_ready()
    fe_race = get_fe()
    fone_race = get_fone()
    channel = bot.get_channel(int(CHANNEL_ID))
    if channel:
        await channel.send(fe_race)
        await channel.send('------------------------------------')
        await channel.send(fone_race)

bot.run(TOKEN)