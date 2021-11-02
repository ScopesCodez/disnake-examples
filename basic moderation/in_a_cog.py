import disnake
from disnake.ext import commands

class Moderation(commands.Cog):
    """Moderation cog that has simple few moderation commands as example."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: disnake.Member, *, reason=None):

        # We'll try to send a message to the member that was banned to inform them.
        try:
            await member.send(f"You have been banned from **{ctx.guild}**!\nReason: {reason}")
        except disnake.Forbidden:
            # If the bot couldn't send a message to the user, we'll just ignore it.
            print(f"Dms are disabled of {member} : {member.id}")

        await member.ban(reason=reason)

        await ctx.send(f'**{member} has been banned for:** {reason}')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: disnake.Member, *, reason=None):

        # We'll try to send a message to the member that was kicked to inform them.
        try:
            await member.send(f"You have been kicked from **{ctx.guild}**!\nReason: {reason}")
        except disnake.Forbidden: 
            # If the bot couldn't send a message to the user, we'll just ignore it.
            print(f"Dms are disabled of {member} : {member.id}")

        await member.kick(reason=reason)

        await ctx.send(f'**{member} has been kicked for:** {reason}')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.send(f"**{deleted}** messages have been deleted!", delete_after=3)


def setup(bot):
    bot.add_cog(Moderation(bot))