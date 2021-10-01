# Inspired by discord music bot project found here
# https://github.com/joek13/py-music-bot

import discord
from discord.ext import commands
from cogs.Music._helpers.Song import Song

class Music(commands.Cog):

    def __init__(self, client, config):
        self.client = client
        self.config = config
        self.nowPlaying = None
        self.playlist = []
        self.volume = 1.0
        self.voiceClient = None

    def _findNextSong(self):
        if len(self.playlist) > 0:
            song = self.playlist[0]
            del(self.playlist[0])
            return song

    def _playSong(self, song):
        self.nowPlaying = song
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.url), volume=self.volume)
        
        def _playNext(err):
            self.nowPlaying = None
            song = self._findNextSong()
            # Only start playing if there was a valid song
            if song:
                self._playSong(song)
                return
            # If there were no valid songs, start the idle timeout
            
            # ADD TIMEOUT HERE IT WILL RUN THIS AFTER 5 MINS AND DISCONNECT
            self.voiceClient = None

        self.voiceClient.play(source, after=_playNext)

        
    @commands.command("play")
    async def play(self, ctx, *, searchTerm=None):
        voiceClient = ctx.guild.voice_client

        # Only users currently in a voice channel can add to the queue
        if ctx.author.voice is not None and ctx.author.voice.channel is not None:

            # Sometimes if a lot of songs are added at once the bot gets stuck with songs in the queue
            # but not playing anything. Kick start it by calling play command without args
            if searchTerm == None:
                if self.voiceClient and not self.nowPlaying:
                    song = self._findNextSong()
                    if song:
                        self._playSong(song)
                # Regardless of whether we play or not, we return to make sure we don't try to search for
                # a song with a None search term
                return
            
            # If the bot is already playing a song, add it to the queue
            if voiceClient and voiceClient.channel:
                try:
                    song = Song(searchTerm, ctx.author)
                except youtube_dl.DownloadError as e:
                    await ctx.send("Couldn't find a video using that search term")
                    return
                self.playlist.append(song)
                message = await ctx.send("Added to queue", embed=song.getEmbed())
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
                self.voiceClient = await channel.connect()
                self._playSong(song)
                message = await ctx.send("", embed=song.getEmbed())
                #await self._add_reaction_controls(message)
        else:
            await ctx.send("You need to be in a voice channel to send this command")
