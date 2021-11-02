import disnake
from disnake.ext import commands

class ErrorHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        should_raise = False
        
        if isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.MissingRequiredArgument):
            err = f"`{error.missing_param}` is a required argument that is missing!"

        elif isinstance(error, commands.BadArgument):
            err = f"`{error.param}` is not a valid argument!"

        elif isinstance(error, commands.MissingPermissions):
            err = f"You need `{', '.join(error.missing_perms)}` permission(s) to use this command!"

        elif isinstance(error, commands.MemberNotFound):
            err = f"I couldn't find member **{error.param}**!"
            
        elif isinstance(error, commands.UserNotFound):
            err = f"I couldn't find user **{error.param}**!"

        else:
            err = f"An unknown error has occurred!\n```\n{error}\n```"
            should_raise = True

        embed = disnake.Embed(color=discord.Color.red(), description=err)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)
        if should_raise:
            raise error

def setup(bot):
    bot.add_cog(ErrorHandling(bot))
