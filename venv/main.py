import discord
import os
import asyncio
import random
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!',intents =discord.Intents.all())


@bot.event
async def on_ready():
    print("Bot is connected to discord!!")


@bot.event
async def on_message(msg):
    user_msg=str(msg.content)
    user=str(msg.author)
    if user==bot.user:
        return
    else:
        if user_msg=="hello":
            await msg.channel.send("hai")




bot.run(token)