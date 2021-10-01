import discord, json
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, client, config):
        self.client = client
        self.config = config
