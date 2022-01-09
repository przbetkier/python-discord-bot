from discord.ext import commands
import re
from datetime import datetime, timedelta
import csv


class Remind(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Remind command ready")

    @commands.command()
    async def remind(self, ctx, *args):
        author = ctx.message.author.mention

        if len(args) < 2:
            await ctx.message.channel.send("Please enter all args")
            return

        if is_time_arg_valid(args[1]):
            reminder_message = args[0]
            time = parse_time(args[1])

            with open(r'reminders.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([author, reminder_message, ctx.message.channel.id, round(time.timestamp())])
                await ctx.message.channel.send("Gotcha {0}, I will remind you 👌".format(ctx.message.author.mention))
        else:
            await ctx.message.channel.send(
                "Invalid command format. Proper format looks like `!remind \"Buy milk!\" 10m` \nValid time: `s` or `m` or `h`"
            )


def is_time_arg_valid(arg):
    return len(re.findall(r'\d+[s|m|h]', arg)) > 0


def parse_time(time):
    digits = int(re.findall(r'\d+', time)[0])
    if time.endswith('s'):
        return datetime.now() + timedelta(seconds=digits)
    elif time.endswith('m'):
        return datetime.now() + timedelta(minutes=digits)
    elif time.endswith('h'):
        return datetime.now() + timedelta(hours=digits)
    elif time.endswith('d'):
        return datetime.now() + timedelta(days=digits)


def setup(client):
    client.add_cog(Remind(client))
