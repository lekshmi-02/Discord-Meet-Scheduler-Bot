from discord.ext import commands
import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ui import Button,View

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
pollid = os.getenv('POLL_CHANNEL')
annonid = os.getenv('ANNOUNCEMENT_CHANNEL')
botid = os.getenv('BOT_ID')