import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix='...', intents=disnake.Intents.default(members=True))

# ...

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: disnake.Member, *, reason=None):

    # We'll try to send a message to the member that was banned to inform them.
    try:
        await member.send(f"You have been banned from **{ctx.guild}**!\nReason: {reason}")
    except:
        # If the bot couldn't send a message to the user, we'll just ignore it.
        pass

    await member.ban(reason=reason)

    await ctx.send(f'**{member} has been banned for:** {reason}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: disnake.Member, *, reason=None):

    # We'll try to send a message to the member that was kicked to inform them.
    try:
        await member.send(f"You have been kicked from **{ctx.guild}**!\nReason: {reason}")
    except:
        # If the bot couldn't send a message to the user, we'll just ignore it.
        pass

    await member.kick(reason=reason)

    await ctx.send(f'**{member} has been kicked for:** {reason}')

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"**{deleted}** messages have been deleted!", delete_after=3)


# ...    