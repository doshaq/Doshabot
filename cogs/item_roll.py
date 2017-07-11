from discord.ext import commands
import random as rng
import discord
import random

class item_roll:
	"""Utilities that provide pseudo-RNG."""
	def __init__(self, bot):
		self.bot = bot		
	@commands.group(pass_context=True)
	async def random(self, ctx):
		"""Displays a random thing you request."""
		if ctx.invoked_subcommand is None:
			await self.bot.say('امرك خطاء ياصاحبي.')
	@commands.command()
	async def lenny(self):
		"""Displays a random lenny face."""
		lenny = rng.choice([
            "( ͡° ͜ʖ ͡°)", "( ͠° ͟ʖ ͡°)", "ᕦ( ͡° ͜ʖ ͡°)ᕤ", "( ͡~ ͜ʖ ͡°)",
            "( ͡o ͜ʖ ͡o)", "͡(° ͜ʖ ͡ -)", "( ͡͡ ° ͜ ʖ ͡ °)﻿", "(ง ͠° ͟ل͜ ͡°)ง",
            "ヽ༼ຈل͜ຈ༽ﾉ"
        ])
		await self.bot.say(lenny)
	@commands.command(pass_context=True)
	async def roll(self,ctx,member: discord.Member = None):
			if member is None:
				member = ctx.message.author
				dice   = random.randint(0,100)
			await self.bot.say('{0.mention} rolled '.format(member) +  str(dice))
def setup(bot):
    bot.add_cog(item_roll(bot))