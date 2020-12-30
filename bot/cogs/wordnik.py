import os
import aiohttp
from discord.ext.commands import Cog, Context, command


class Wordnik(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.wordnik_key = os.environ["WORDNIK_API_KEY"]

    @command()
    async def define(self, ctx: Context, *, word: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.wordnik.com/v4/word.json/{word}/definitions?limit=3&includeRelated=false&sourceDictionaries=all&useCanonical=false&includeTags=false&api_key={self.wordnik_key}") as response:
                if response.status != 200:
                    return await ctx.send(f"{response.status} Could not uhhhhhhhhhhhh yea")
                definitions = await response.json()
                i = 0
                for definition in definitions:
                    try:
                        txt: str = definition["text"]
                        txt = txt.replace("<em>", "*")
                        txt = txt.replace("</em>", "*")
                        partOfSpeech = definition["partOfSpeech"]
                        await ctx.send(f"definition: **{partOfSpeech}** {txt}")
                    except:
                        i += 1

                    if i == len(definitions):
                        await ctx.send("No definitions found")


    @command(aliases=["wordoftheday", "word-of-the-day", "wordOfTheDay", "Word-Of-The-Day"])
    async def word_of_the_day(self, ctx: Context):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key={self.wordnik_key}") as response:
                if response.status != 200:
                    return await ctx.send("IDK")
                wordOfTheDay = await response.json()
                word = wordOfTheDay["word"]
                await ctx.send(f"word of the day: {word}")
                definitions = wordOfTheDay["definitions"]
                for i in range(len(definitions)):
                    await ctx.send(f"definition {i+1}: {definitions[i]['text']}")


    @command(aliases=["randomword", "randomWord", "random-word"])
    async def random_word(self, ctx: Context):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&api_key={self.wordnik_key}") as response:
                word = await response.json()
                word = word["word"]

                await ctx.send(word)

                await self.define(ctx, word=word)






def setup(bot):
    bot.add_cog(Wordnik(bot))