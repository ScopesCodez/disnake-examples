# Creating your first ever Discord bot in Python? This is how you do it!

# First, you'd need to import the required libraries. We will use 'disnake', which you can install by executing `pip install disnake` in your command prompt/terminal.

import disnake
from disnake.ext import commands
import asyncio

# Now we will create our bot instance! This will be the object that represents our Discord bot in the code.
bot = commands.Bot(command_prefix='!', intents=disnake.Intents.default(members=True))
# Make sure you go to https://discord.com/developers/applications/your_bot_id/bot and scroll down to "Privilaged Intents" and enable the "Member intents"!

# We will create an async function that will be executed once our bot is online.

async def startup_function():
    # We will let it wait until the bot is fully loaded.
    await bot.wait_until_ready()
    # Now let's set the bot's status to online and the game activity to '!help'
    await bot.change_presence(status=disnake.Status.online, activity=disnake.Game(name='!help'))

# Now, we want to know when our bot has started up. We will use the 'on_ready' event.
@bot.event
async def on_ready():
    print("Logged in as\n", bot.user, "\n", bot.user.id, "-------------")

# Let's make a simple 'ping' command that shows the bot's latency.
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

# Now let's make our startup_function() run!
bot.loop.create_task(startup_function())

# And finally, we'll run our bot!
bot.run("YOUR BOT'S TOKEN")