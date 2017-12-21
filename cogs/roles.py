from discord.ext import commands
import random as rng
import discord
import random
import webcolors
class roles:
	def __init__(self, bot):
		self.bot = bot		
	@commands.command(pass_context=True)
	async def role(self,ctx,*keywords):
			ctx_server = ctx.message.server
			ctx_channel= ctx.message.channel
			entered_role = keywords[0]
			print(entered_role)
			role = discord.utils.get(ctx_server.roles, name=entered_role)			
			if role is None:
				# If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
				await self.bot.say("اسم الرول خطاء ياليت تتاكد")
				return
			elif role in ctx.message.author.roles:
				# If they already have the role
				await self.bot.say("الرول معك حاليا")
			else:
				try:
					await self.bot.add_roles(ctx.message.author, role)
					await self.bot.say("{0}  اضفت لك الرول  {1.mention} ".format(entered_role,ctx.message.author))
				except discord.Forbidden:
					await self.bot.say("ماعندي صلاحيه كلم الادمن سريع")


	@commands.command(pass_context=True)
	async def color(self,ctx,*keywords):
		ctx_server = ctx.message.server
		ctx_channel= ctx.message.channel
		entered_role = keywords[0]	
		col = discord.Colour(value = int((webcolors.name_to_hex('black')[1:]),16))
		
		if '#' not in entered_role:
			col = discord.Colour(value = int((webcolors.name_to_hex(entered_role)[1:]),16))
		else:
			col = discord.Colour(value = int(entered_role[1:],16))
		colors = discord.utils.get(ctx_server.roles, name="col_"+entered_role)			
		if colors is None:
			# If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
			#create the color on roles
			Role_color=	await self.bot.create_role(ctx_server)
			await self.bot.edit_role(ctx_server, Role_color, name="col_"+entered_role, colour = col)

			#userroles = discord.utils.find(ctx.message.author.roles,name=("%col%"))
			for r in ctx.message.author.roles:
				 if "col" in r.name:
					 print("removing color")
					 await self.bot.remove_roles(ctx.message.author,r)
			
			await self.bot.add_roles(ctx.message.author, Role_color)
			await self.bot.say("{0}  اضفت لك اللون  {1.mention} ".format(entered_role,ctx.message.author))


		elif colors in ctx.message.author.roles:
			# If they already have the role
			await self.bot.say("اللون معك حاليا")


		else:
			try:#add the color from the made list
				for r in ctx.message.author.roles:
					if "col" in r.name:
						await	self.bot.remove_roles(ctx.message.author,r)
				await self.bot.add_roles(ctx.message.author, colors)
				await self.bot.say("{0}  اضفت لك اللون  {1.mention} ".format(entered_role,ctx.message.author))
			except discord.Forbidden:
				await self.bot.say("ماعندي صلاحيه كلم الادمن سريع")

		
	@commands.command(pass_context=True)
	async def removec(self,ctx):
			for r in ctx.message.author.roles:
				if "col" in r.name:
					print("removing color")
					await self.bot.remove_roles(ctx.message.author,r)
			await self.bot.say("تم حذف اللألوان")

	@commands.command(pass_context=True)
	async def cleanc(self,ctx):
		print("doing it")
		message   = await self.bot.say("سيتم حذف الالوان....")
		server    = ctx.message.server
		usr_roles = ctx.message.channel.permissions_for(ctx.message.author)
		if not usr_roles.administrator:
				await self.bot.say(" ماعندك صلاحيه للشي هذا ")
				return			
		x = 0
		for r in server.roles:
			print(str(r))
			
			if "col" in r.name and r is not None:
				for users in server.members:
					if r not in users.roles:
						x+=1
						print("removing color")
						if r in server.roles:
							await self.bot.delete_role(ctx.message.server,r)
	
		await self.bot.edit_message(message," لون {0} تم حذف ".format(str(x)))	


def setup(bot):
    bot.add_cog(roles(bot))