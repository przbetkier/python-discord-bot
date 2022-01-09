import os
from dotenv import load_dotenv
from discord.ext.tasks import loop
from tasks import reminder
from discord.ext import commands

load_dotenv()

SERVER_NAME = os.getenv('SERVER_NAME')
TOKEN = os.getenv('AUTH_TOKEN')
bot = commands.Bot(command_prefix='!')

# load all cogs from cogs directory
for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        bot.load_extension("cogs." + f[:-3])


@bot.event
async def on_ready():
    print("Logged on {0}!".format(SERVER_NAME))


@loop(seconds=1)
async def reminder_task():
    await reminder.remind(bot)


@reminder_task.before_loop
async def reminder_before():
    global bot
    await bot.wait_until_ready()


def main():
    reminder_task.start()
    bot.run(TOKEN)


if __name__ == "__main__":
    main()
