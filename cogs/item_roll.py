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
		emote = ""
		if member is None:
			member = ctx.message.author
			dice   = random.randint(0,100)
			if dice >= 90:
				emote=":shamrock:"
			elif dice <= 30:
				emote=":poop:"
			else:
				emote=":game_die:"
			await self.bot.say('{0.mention} rolled : {1}  {2}'.format((member) , str(dice), emote))
def setup(bot):
    bot.add_cog(item_roll(bot))