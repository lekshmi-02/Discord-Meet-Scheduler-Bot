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


# @bot.event
# async def on_message(msg):
#     user_msg=str(msg.content)
#     user=str(msg.author)
#     if user==bot.user:
#         return
#     else:
#         if user_msg=="hello":
#             await msg.channel.send("hai")
def convert_time(hr,min):
    hr=int(input[0:2])
    min=int(input[2:])
    postfix="PM"
    if hr<12:
        postfix="AM"
        hr-=12
    return '{}:{:02d}'.format(hr or 12,min,postfix)
def convert_date(date,month,year):
    # year=int(input[0:4])
    # month=int(input[4:6])
    # date=int(input[6:8])
    
    return '{}/{}/{}'.format(date,month,year)

@bot.command()
async def date(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel==ctx.channel
    await ctx.send("Enter the date of meeting")
    dateinput = await bot.wait_for("message",check=check)
    date = dateinput.content
    monthinput = await bot.wait_for("message",check=check)
    month = monthinput.content
    yearinput = await bot.wait_for("message",check=check)
    year = yearinput.content
    global formatteddate
    formatteddate = convert_date(date,month,year)
    await ctx.send(formatteddate)

@bot.command()
async def time(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel==ctx.channel
    
    await ctx.send("Enter the time of meeting")
    hourinput = await bot.wait_for("message",check=check)
    hour = hourinput.content
    minuteinput = await bot.wait_for("message",check=check)
    min = minuteinput.content
    formattedtime = convert_time(hour,min)
    await ctx.send(formattedtime)

@bot.command()
async def poll(ctx):
    emb=discord.Embed(title="Poll for meeting",description=f" A meeting is about to be scheduled on {formatteddate}\n Do you want to join?")
    
    poll_channel = bot.get_channel('POLL_CHANNEL')
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await asyncio.sleep(10)
    await ctx.send("Oops!! Time is up")

    
bot.run(token)