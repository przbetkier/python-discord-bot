from discord.ext import commands
from discord.ext.commands import Cog
import requests
import json


class Quote(Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Quotes cog ready")

    @commands.command()
    async def quote(self, ctx):
        quote_msg = await get_quote()
        await ctx.message.channel.send(quote_msg)


async def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = json.loads(response.text)
    quote = data[0]['q']
    author = data[0]['a']
    return "_{0}_ - **{1}**".format(quote, author)


def setup(client):
    client.add_cog(Quote(client))
