from discord.ext import commands
from discord.ext.commands import Cog


class Swears(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        print("Swears cog ready")

    @Cog.listener("on_message")
    async def warn(self, message):
        swears = load_swears()
        words = map(lambda word: word.lower(), message.content.split())

        has_swears = any(word in swears for word in words) and not message.content.startswith("!curses")
        if has_swears and message.author != self.client.user:
            await message.channel.send('Please, behave {0}! 😡'.format(message.author.mention))


def load_swears():
    with open("curses.txt", "r") as file:
        return file.read().splitlines()


def setup(client):
    client.add_cog(Swears(client))
