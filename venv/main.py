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

'''
@bot.event
async def on_message(msg):
    user_msg=str(msg.content)
    user=str(msg.author)
    if user==bot.user:
        return
    else:
        if user_msg=="hello":
            await msg.channel.send("hai")
'''
@bot.command()
async def hello(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel==ctx.channel
    await ctx.send("Enter the starting date of meeting")
    startinput = await bot.wait_for("message",check=check)
    startdate = startinput.content
    await ctx.send("Enter the ending date of meeting")
    endinput = await bot.wait_for("message",check=check)
    edate = endinput.content
    await ctx.send("Enter the starting time of meeting")
    stimeinput = await bot.wait_for("message",check=check)
    starttime = stimeinput.content
    await ctx.send("Enter the ending time of meeting")
    etimeinput = await bot.wait_for("message",check=check)
    endtime = etimeinput.content

    # date = input()
    # print(date)
    
bot.run(token)