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






def convert_time(hr,min):
    hr=int(input[0:2])
    min=int(input[2:])
    postfix="PM"
    if hr<12:
        postfix="AM"
    return '{}:{:02d}{}'.format(hr or 12,min,postfix)
def convert_date(date,month,year):
    year=int(input[0:4])
    month=int(input[4:6])
    date=int(input[6:8])
    
    return '{}/{}/{}'.format(date,month,year)



@bot.event()
async def poll(ctx,message):
    emb=discord.Embed(title="poll for meeting",description=f"{message}")
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')

bot.run(token)