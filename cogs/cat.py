from discord.ext import commands
from discord.ext.commands import Cog
from discord import File
import requests
import json
import os


class Cat(Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cat cog ready")

    @commands.command()
    async def cat(self, ctx):
        await get_cat()
        file = File("cat.jpg")
        await ctx.send(file=file, content="Here is a kitty for ya!")
        # remove file when attachment sent
        os.remove("cat.jpg")


async def get_cat():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = json.loads(response.text)
    url = data[0]['url']
    cat_img = requests.get(url)
    if cat_img.status_code == 200:
        # write binary data to cat.jpg
        with open("cat.jpg", 'wb') as f:
            f.write(cat_img.content)
            return f


def setup(client):
    client.add_cog(Cat(client))
