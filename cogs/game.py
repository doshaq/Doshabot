from discord.ext import commands
import sqlite3
class game :
	conn = sqlite3.connect('bot_game.db')
	c = conn.cursor()
	def __init__(self, bot):
		self.bot = bot
		conn = sqlite3.connect('bot_game.db')
		c = conn.cursor()
	@commands.command(pass_context=True, no_pm=True)
	async def join_game(self, ctx, *keywords):
		self.c.execute("INSERT INTO players VALUES('{}','{}','{}','talking_island',1,NULL,'false')".format(str(ctx.message.author),keywords[0],keywords[1]))
		self.conn.commit()
		await self.bot.say("تم اضافتك للعبه")
	@commands.command(pass_context=True,no_pm=True)
	async def login(self,ctx):
		self.c.execute("UPDATE players SET connect='true' WHERE username ='{}'".format(str(ctx.message.author)))
		self.conn.commit()
		await self.bot.say("تم الاتصال")
	@commands.command(pass_context=True,no_pm=True)
	async def logout(self,ctx):
		self.c.execute("UPDATE players SET connect='false' WHERE username ='{}'".format(str(ctx.message.author)))
		self.conn.commit()
		await self.bot.say("تم قطع الاتصال")
def setup(bot):
    bot.add_cog(game(bot))