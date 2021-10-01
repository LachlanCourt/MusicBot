# Inspired by discord music bot project found here
# https://github.com/joek13/py-music-bot

import discord
from discord.ext import commands
from cogs._helpers.video import Video

class Music(commands.Cog):

    def __init__(self, client, config):
        self.client = client
        self.config = config
        self.now_playing = None
        self.playlist = []

    def _play_song(self, client, song):
        self.now_playing = song
        source = discord.PCMVolumeTransformer(
            discord.FFmpegPCMAudio(song.stream_url, volume=1.0)

        client.play(source, after=after_playing)

    async def play(self, ctx, *, url):
        client = ctx.guild.voice_client

        if client and client.channel:
            try:
                video = Video(url, ctx.author)
            except youtube_dl.DownloadError as e:
                await ctx.send("Couldn't find a video using that search term!")
                return
            self.playlist.append(video)
            message = await ctx.send("Added to queue.", embed=video.get_embed())
            #await self._add_reaction_controls(message)
        else:
            if ctx.author.voice is not None and ctx.author.voice.channel is not None:
                channel = ctx.author.voice.channel
                try:
                    video = Video(url, ctx.author)
                except youtube_dl.DownloadError as e:
                    await ctx.send("Error downloading video")
                    return
                client = await channel.connect()
                self._play_song(client, video)
                message = await ctx.send("", embed=video.get_embed())
                #await self._add_reaction_controls(message)
            else:
                await ctx.send("You need to be in a voice channel to send this command")
