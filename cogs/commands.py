from discord.ext import commands
from discord.ext.commands import Cog

config = {
    '!cat': 'Kitty photo for everybody!',
    '!quote': 'Returns random quote',
    '!remind [reminder, delta]': 'Helps you remember about important stuff!',
    '!play [url]': 'Play music on voice channel',
    '!pause': 'Pause music on voice channel',
    '!resume': 'Resume music on voice channel',
    '!stop': 'Stop music on voice channel',
    '!leave': 'Disconnect bot from voice channel',
}


class Commands(Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Commands cog ready")

    @commands.command()
    async def commands(self, ctx):
        commands_hint_message = "```"
        for command, description in config.items():
            commands_hint_message += "!{0} - {1}\n".format(command, description)
        commands_hint_message += "```"
        await ctx.message.channel.send(commands_hint_message)


def setup(client):
    client.add_cog(Commands(client))
