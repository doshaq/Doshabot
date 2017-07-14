from discord.ext import commands
from random import choice, shuffle
import aiohttp
import functools
import asyncio

class msc :

	def __init__(self, bot):
		self.bot = bot
	@commands.command(pass_context=True)
	async def troll(self,ctx,*keywords):
		if keywords:
			keywords = "+".join(keywords)
		else:
			await self.bot.send_cmd_help(ctx)
			return

		await self.bot.say("hello there ")
    
def setup(bot):
    bot.add_cog(msc(bot))