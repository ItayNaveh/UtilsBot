from discord import Embed, Message, RawReactionActionEvent
from discord.ext.commands import Cog, Context, command

reactions = {
    "💻": 764203465882075136,
    "⚙️": 123
}

class ReactionRoles(Cog):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def here(self, ctx: Context):
        

        embed = Embed()

        embed.title = "title"
        embed.description = "desc"

        msg: Message = await ctx.send(embed=embed)
        for emoji in reactions:
            await msg.add_reaction(emoji)


    @Cog.listener()
    async def on_raw_reaction_add(self, payload: RawReactionActionEvent):
        if (payload.member.bot == False):
            print(payload.emoji)





def setup(bot):
    bot.add_cog(ReactionRoles(bot))