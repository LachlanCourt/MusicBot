# Inspired by discord music bot project found here
# https://github.com/joek13/py-music-bot

import discord
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, client, config):
        self.client = client
        self.config = config
