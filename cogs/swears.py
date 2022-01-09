from discord.ext import commands
from discord.ext.commands import Cog


class Swears(commands.Cog):
    def __init__(self, client):
        self.client = client  # sets the client variable so we can use it in cogs

    @commands.Cog.listener()
    async def on_ready(self):
        print("Swears cog ready")

    @Cog.listener("on_message")
    async def warn(self, message):
        swears = load_swears()
        words = message.content.split()

        has_swears = any(word in swears for word in words)
        if has_swears:
            await message.channel.send('Please, behave {0}! 😡'.format(message.author.mention))


def load_swears():
    with open("curses.txt", "r") as file:
        return file.read().splitlines()


def setup(client):
    client.add_cog(Swears(client))
