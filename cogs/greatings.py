from discord.ext import commands


class greatings :

	def __init__(self, bot):
		self.bot = bot
	@commands.command()
	async def hello(self):
		await self.bot.say("hello there ")
	@commands.command()
	async def hi(self):
		await self.bot.say("hi")

    
def setup(bot):
    bot.add_cog(greatings(bot))