# Inspired by discord music bot project found here
# https://github.com/joek13/py-music-bot

import discord
from discord.ext import commands
from cogs.Music._helpers.Song import Song

class Music(commands.Cog):

    def __init__(self, client, config):
        self.client = client
        self.config = config
        self.now_playing = None
        self.playlist = []
        self.volume = 1.0

    def _play_song(self, voiceClient, song):
        self.now_playing = song
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.url), volume=self.volume)
        voiceClient.play(source)

    @commands.command("play")
    async def play(self, ctx, *, searchTerm):
        voiceClient = ctx.guild.voice_client

        # Only users currently in a voice channel can add to the queue
        if ctx.author.voice is not None and ctx.author.voice.channel is not None:
            # If the bot is already playing a song, add it to the queue
            if voiceClient and voiceClient.channel:
                try:
                    song = Song(searchTerm, ctx.author)
                except youtube_dl.DownloadError as e:
                    await ctx.send("Couldn't find a video using that search term")
                    return
                self.playlist.append(song)
                message = await ctx.send("Added to queue.", embed=song.getEmbed())
                #await self._add_reaction_controls(message)
            # If the bot is not currently playing a song, start it playing straight away
            else:
            
                channel = ctx.author.voice.channel
                try:
                    song = Song(searchTerm, ctx.author)
                except youtube_dl.DownloadError as e:
                    await ctx.send("Error downloading video")
                    return
                # The bot has joined a new voice channel so we should clear the old playlist
                self.playlist = []
                voiceClient = await channel.connect()
                self._play_song(voiceClient, song)
                message = await ctx.send("", embed=song.getEmbed())
                #await self._add_reaction_controls(message)
        else:
            await ctx.send("You need to be in a voice channel to send this command")
