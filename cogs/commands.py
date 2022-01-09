from discord.ext import commands
from discord.ext.commands import Cog

config = {
    'quote': 'Returns random quote',
    'remind': 'Helps you remember about important stuff!'
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
