from discord.ext import commands
from random import choice, shuffle
import aiohttp
import functools
import asyncio
import xml.etree.ElementTree as elt
import spice_api as spice
import DoshaBot
import dataIO
from __main__ import send_cmd_help, settings

class MAL :
	def __init__(self, bot):
		self.bot   = bot
		self.credentials = dataIO.load_json("data/api/keys.json")
		self.creds = spice.init_auth(credentials["mal_username"],credentials["mal_password"]) 

	@commands.command(pass_context=True, no_pm=True)
	async def malsearch(self, ctx, *keywords):
		await self.bot.say("searching....")
		if keywords:
			keywords = "+".join(keywords)
		else:
			await send_cmd_help(ctx)
			return
		results = spice.search(keywords, spice.get_medium('anime'),creds)
		await self.bot.say(results[0].image_url+"\n"+
		"__**" + results[0].title+"__** \n"
		 + "  تقيمه " + results[0].score +"\n"
		 +"```"+results[0].synopsis+"```"+"\n")
		
	@commands.command(pass_context=True, no_pm=True)
	async def mal(self, ctx, *keywords):
		await self.bot.say("malsearch [what u want to search]....")
		
def setup(bot):
    bot.add_cog(MAL(bot))