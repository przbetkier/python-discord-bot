from discord.ext import commands
from discord.ext.commands import Cog


class Curses(Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        print("Curses cog ready")

    @commands.command()
    async def curses(self, ctx, *args):
        curses_list = list_curses()
        if len(args) == 0 or (len(args) == 1 and args[0] == "list"):
            curses = '\n'.join(curses_list)
            await ctx.message.channel.send("Currently I react for these curses:\n" + curses)
        elif len(args) >= 2 and args[0] == 'add':
            curse_to_add = args[1]
            if curse_to_add in curses_list:
                await ctx.message.channel.send("Curse {0} already on list".format(curse_to_add))
                return
            else:
                add_curse(curse_to_add)
                await ctx.message.channel.send("Added curse `{0}` on list".format(curse_to_add))
                return
        elif len(args) >= 2 and args[0] == 'remove':
            curse_to_remove = args[1]
            if curse_to_remove not in curses_list:
                await ctx.message.channel.send(
                    "Can't remove `{0}` because it's not on the forbidden words list.".format(curse_to_remove))
                return
            else:
                remove_curse(curse_to_remove, curses_list)
                await ctx.message.channel.send("Removed curse `{0}` from list".format(curse_to_remove))
                return


def list_curses():
    with open("curses.txt", "r") as file:
        return file.read().splitlines()


def add_curse(curse):
    # 'a' for append mode while editing file
    with open("curses.txt", "a") as file:
        file.write("{0}\n".format(curse))


def remove_curse(curse, curses_list):
    # remove given curse from all curses list
    curses_to_save = list(filter(lambda c: c != curse, curses_list))
    # rewrite file
    with open("curses.txt", "w") as file:
        for curse in curses_to_save:
            file.write("{0}\n".format(curse))


def setup(client):
    client.add_cog(Curses(client))
