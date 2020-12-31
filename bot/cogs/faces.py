from discord import Message
from discord.ext.commands import Cog


class Faces(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_message(self, msg: Message):
        faces = []
        for face in faces:
            if face in msg.content:
                await msg.add_reaction("")





def setup(bot):
    bot.add_cog(Faces(bot))