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
	@commands.command()
	async def commands(self):
		await self.bot.say("```roll:\nيختار لك رقم عشوائي بين 0 وال100\n role:\nتاخذ رول معين اذا مسموح لك\ncolor:\nتحط لون لنفسك\nremovec :\nتشيل اللون من نفسك\n```")
    
def setup(bot):
    bot.add_cog(greatings(bot))