import discord
import os
import asyncio
import random
from dotenv import load_dotenv
from discord.ext import commands



load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot_id = os.getenv('BOT_ID')
poll_id = os.getenv('POLL_ID')
ann_id = os.getenv('ANN_ID')
# poll_id = os.getenv('POLL_CHANNEL')

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
    # hr,min =int(input[0:2]);int(input[2:4])
    postfix="AM"
    if hr>12:
        postfix="PM"
        hr-=12
    return '{}:{:02d} {}'.format(hr or 12,min,postfix)
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
    hour = int(hourinput.content)
    minuteinput = await bot.wait_for("message",check=check)
    min = int(minuteinput.content)
    global formattedtime 
    formattedtime= convert_time(hour,min)
    await ctx.send(formattedtime)


@bot.command()
async def poll(ctx):
    
    emb = discord.Embed(title="Poll for meeting",description=f" A meeting is about to be scheduled on {formatteddate} at {formattedtime} at  \n Do you want to join?")
    channel= bot.get_channel(int(poll_id))
    msg = await channel.send(embed = emb)
    await ctx.send("Poll has begun!!")
    up = '👍'
    down = '👎'
    await msg.add_reaction(up)
    await msg.add_reaction(down)
    await asyncio.sleep(30)

    await channel.send("Oops!! Time is up")
    user = bot.get_user(int(bot_id))
    users=[]
    message = await msg.channel.fetch_message(msg.id)
    for reaction in message.reactions:
        if reaction.emoji == up:
            yes = reaction.count
            async for i in reaction.users():
                users.append(user)

        if reaction.emoji == down:
            no = reaction.count
    if yes>no:
        ann_channel = bot.get_channel(int(ann_id))
        await ann_channel.send("Meet Scheduled")
    



    # def check(reaction,user):
    #     return user == ctx.author and str(reaction.emoji) in [up,down]
    

    # mem = ctx.author

    # while True :
    #     reaction,user = await bot.wait_for("reaction_add",timeout = 30.0, check = check)

    #     if(str(reaction.emoji)==up):
    #         await ctx.send("Thankyou")
    #     if(str(reaction.emoji)==down):
    #         await ctx.send("Welcome")





    # message = await ctx.channel.fetch_message(msg.id) 
    # user = bot.get_user(int(bot_id))
    # yes = 0
    # no = 0
    # for r in message.reactions:
    #     if r.emoji == '👍':
    #         yes +=1
    #     if r.emoji == '👎':
    #         no +=1

    # if(yes>no):
    #     await ctx.send("hello")

bot.run(token)