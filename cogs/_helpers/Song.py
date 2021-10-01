import youtube_dl as ytdl
import discord

class Song:

    def __init__(self, searchTerm, requestedBy):
        videoInfo = self._get_info(searchTerm)
        video = videoInfo["formats"][0]
        self.url = video["url"]
        self.title = videoInfo["title"]
        self.uploader = ""
        if "uploader" in videoInfo:
            self.uploader = videoInfo["uploader"]
        self.thumbnail = None
        if "thumbnail" in videoInfo:
            self.thumbnail = videoInfo["thumbnail"]
        self.requestedBy = requestedBy

    def _get_info(self, video_url):
        options = {"default_search": "ytsearch", "format": "bestaudio/best", "quiet": True, "extract_flat": "in_playlist"}
        with ytdl.YoutubeDL(options) as ydl:
            videoInfo = ydl.extract_info(video_url, download=False)
            if "_type" in videoInfo and videoInfo["_type"] == "playlist":
                return self._get_info(videoInfo["entries"][0]["url"])  # get info for first video
            else:
                return videoInfo

    def get_embed(self):
        embed = discord.Embed(title=self.title, description=self.uploader)
        embed.set_footer(text=f"Requested by {self.requestedBy.name}", icon_url=self.requestedBy.avatar_url)
        if self.thumbnail:
            embed.set_thumbnail(url=self.thumbnail)
        return embed
