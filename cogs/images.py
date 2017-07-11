from discord.ext import commands
from random import choice, shuffle
import aiohttp
import functools
import asyncio

GIPHY_API_KEY = "c510a9e0254649f6b3a460123d4f5b8d"


filters = ['fuck','sex','penis','hentai','yaoi','pornhub','xnxx','oppai','pornhub','xnxx',]

class images:
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True, no_pm=True)
    async def gif(self, ctx, *keywords):
        """Retrieves first search result from giphy"""
        if keywords:
            keywords = "+".join(keywords)
        else:
            await self.bot.send_cmd_help(ctx)
            return
        if keywords in filters:
            await self.bot.say("عييب ( ͡ಠ ʖ̯ ͡ಠ).")
            return

        url = ("http://api.giphy.com/v1/gifs/search?&api_key={}&q={}"
               "".format(GIPHY_API_KEY, keywords))

        async with aiohttp.get(url) as r:
            result = await r.json()
            if r.status == 200:
                if result["data"]: 
                    if keywords not in filters:
                        await self.bot.say(result["data"][0]["url"])
                else:
                    await self.bot.say("مالقيت شي ( ͡ಠ ʖ̯ ͡ಠ).")
            else:
                await self.bot.say("حصلت مشكله فالاتصال (ノ°Д°）ノ︵")
    @commands.command(pass_context=True, no_pm=True)
    async def gifr(self, ctx, *keywords):
        """Retrieves a random gif from a giphy search"""
        if keywords:
            keywords = "+".join(keywords)
        else:
            await self.bot.send_cmd_help(ctx)
            return
        if keywords in filters:
            await self.bot.say("عييب ( ͡ಠ ʖ̯ ͡ಠ).")
        url = ("http://api.giphy.com/v1/gifs/random?&api_key={}&tag={}"
               "".format(GIPHY_API_KEY, keywords))

        async with aiohttp.get(url) as r:
            result = await r.json()
            if r.status == 200:
                if result["data"]:
                   if keywords not in filters :
                        await self.bot.say(result["data"]["url"])
                else:
                    await self.bot.say("مالقيت شي ( ͡ಠ ʖ̯ ͡ಠ).")
            else:
                await self.bot.say("حصلت مشكله فالاتصال (ノ°Д°）ノ︵")
    
def setup(bot):
	    bot.add_cog(images(bot))
