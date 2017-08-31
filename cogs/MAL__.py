from discord.ext import commands
from random import choice, shuffle
import aiohttp
import functools
import asyncio
import xml.etree.ElementTree as elt
import spice_api as spice
import __main__
from myanimelist.session import Session


s = __main__.s
credentials = __main__.load_credentials()
creds = spice.init_auth(credentials["mal_username"],credentials["mal_password"]) 
class MAL :

	
	def __init__(self, bot):
		self.bot   = bot
		
	@commands.command(pass_context=True, no_pm=True)
	async def malsearch(self, ctx, *keywords):
		if keywords:
			keywords = " ".join(keywords)
		else:
			await self.bot.send_cmd_help(ctx)
			return
		#results = s.search(keywords, spice.get_medium('anime'),creds)
		await self.bot.say(results[1].image_url+"\n"+
		"__**" + results[1].title+"__** \n"
		 + "  تقيمه " + results[0].score +"\n"
		 +"```"+results[1].synopsis+"```"+"\n  " + keywords)
		

def setup(bot):
    bot.add_cog(MAL(bot))