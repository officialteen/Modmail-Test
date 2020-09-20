import discord
from discord.ext import commands,tasks
import asyncio

class StatusFor7S(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @tasks.loop(seconds=10)
    async def start_status(self):
        server = self.bot.get_guild(644687385606488125)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{server.member_count} Members!"))
        await asyncio.sleep(10)

    @commands.group(name="statos")
    async def statos_group(self, ctx):
        pass

    @statos_group.command(name="start")
    async def start_cmd(self, ctx):
        self.start_status.start()
        await ctx.send("Done! Re-run this command if it stops working")

def setup(bot):
    bot.add_cog(StatusFor7S(bot))
