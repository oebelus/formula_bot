import discord
import asyncio
import os
from dotenv import load_dotenv
from utils import get_fe, get_fone

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup(self) -> None:
        self.bg_task = self.loop.create_task(self.background_task())

    async def on_ready(self):
        print('Online')
        await self.setup()

    async def background_task(self):
        print('Background task started')
        await self.wait_until_ready()
        fe_race = get_fe()
        fone_race = get_fone()
        channel = self.get_channel(int(CHANNEL_ID))
        if channel:
            while not self.is_closed():
                await channel.send(fe_race)
                await channel.send('------------------------------------')
                await channel.send(fone_race)
                await asyncio.sleep(60*60*24)

client = MyClient(intents=discord.Intents.default())
client.run(TOKEN)