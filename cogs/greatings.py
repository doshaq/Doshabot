from discord.ext import commands


class greatings :

	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	async def hello(self):
		await self.bot.say("hello there ")
    
def setup(bot):
    bot.add_cog(greatings(bot))