from discord.ext import commands
from discord.ext.commands import Cog


class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Greetings cog ready")

    @Cog.listener("on_message")
    async def greet(self, message):
        cheers = ["Hi", "hi", "Hello", "hello"]
        if message.content in cheers:
            await message.channel.send('Hello again {0}'.format(message.author.mention))


def setup(client):
    client.add_cog(Greetings(client))
