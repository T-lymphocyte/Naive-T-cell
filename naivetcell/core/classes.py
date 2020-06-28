import discord
from discord.ext import commands
from discord.ext.commands import Bot
import json

class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot