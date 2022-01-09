import discord
from discord.ext import commands
from discord.ext.commands import Cog
import os
from youtube_dl import YoutubeDL


class Music(Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Music cog ready")

    @commands.command()
    async def play(self, ctx, url: str):
        song_exists = os.path.isfile("song.mp3")
        if song_exists:
            os.remove("song.mp3")

        voice_channel = discord.utils.get(ctx.guild.voice_channels, name='Ogólne')
        await voice_channel.connect()
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        youtube_dl_options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredquality': '192',
                'preferredcodec': 'mp3',
            }],
        }
        with YoutubeDL(youtube_dl_options) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "music.mp3")
        voice.play(discord.FFmpegPCMAudio("music.mp3"))

    @commands.command()
    async def leave(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()

    @commands.command()
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("Currently no music is playing.")

    @commands.command()
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("Nothing to resume, music is not paused")


def setup(client):
    client.add_cog(Music(client))
