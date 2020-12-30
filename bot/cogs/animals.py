# import requests
import io
import aiohttp

from discord import Message, Embed, File
from discord.ext.commands import Cog, command, Context

# 🐱
# 🐶
class Animals(Cog):
	def __init__(self, bot):
		self.bot = bot

	@command()
	async def cat(self, ctx: Context, *, tag=""):
		async def getCat(url, filename):
			async with aiohttp.ClientSession() as session:
				async with session.get(url) as resp:
					if resp.status != 200:
						return await ctx.send('Could not send cat :(  \neither error or bad options')
					data = io.BytesIO(await resp.read())
					msg: Message = await ctx.send(file=File(data, filename))
					await msg.add_reaction("🐱")

		
		if tag.lower() == "help":
			embed = Embed(title="Help For Cats", description="{ -- } means you need to put yourself a value")

			fields = [
				("{tag}", "A cat with a tag"),
				("gif", "A cat gif"),
				("says/{text}", "A cat saying text"),
				("{tag}/says/{text}", "A cat with a tag saying text"),
			]

			for name, value in fields:
				embed.add_field(name=name, value=value, inline=False)


			embed.set_footer(text="Cats By: https://cataas.com/ \nfor more options go to the link above")

			await ctx.send(embed=embed)
		else:
			if tag != "":
				if "gif" in tag:
					await getCat("https://cataas.com/cat/" + tag.lower(), "cat.gif")
				else:
					await getCat("https://cataas.com/cat/" + tag.lower(), "cat.jpg")
			else:
				await getCat("https://cataas.com/cat", "cat.jpg")


	@command(aliases=["doggo"])
	async def dog(self, ctx: Context, *, arg=""):
		if arg.lower() == "help":
			embed = Embed(title="Help For Doggos")

			fields = [
				("As far as i know there are no options", "boop")
			]

			for name, value in fields:
				embed.add_field(name=name, value=value, inline=False)


			embed.set_footer(text="Doggos By: https://thedogapi.com/ \nfor more information go to the link above")

			await ctx.send(embed=embed)
		else:
			async with aiohttp.ClientSession() as session:
				async with session.get("https://api.thedogapi.com/v1/images/search/") as resp:
					if resp.status != 200:
						return await ctx.send("Could not send doggo :(")
					img = await resp.json()
					img = img[0]
					img = img["url"]
					msg: Message = await ctx.send(img)
					await msg.add_reaction("🐶")





def setup(bot):
	bot.add_cog(Animals(bot))