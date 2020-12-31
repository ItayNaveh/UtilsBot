from typing import Optional

from discord import Message, Embed, Reaction, Member
from discord.ext.commands import Cog, command, Context

class ReactorIsBot(Exception):
    pass

emojiToNum = {
    "1️⃣": 1,
    "2️⃣": 2,
    "3️⃣": 3,
    "4️⃣": 4,
    "5️⃣": 5,
    "6️⃣": 6,
    "7️⃣": 7,
    "8️⃣": 8,
    "9️⃣": 9
}

numToEmoji = {
     1: "1️⃣",
     2: "2️⃣",
     3: "3️⃣",
     4: "4️⃣",
     5: "5️⃣",
     6: "6️⃣",
     7: "7️⃣",
     8: "8️⃣",
     9: "9️⃣"
}

class TicTacToe(Cog):
    def __init__(self, bot):
        self.bot = bot

        self.curPlayer = "X"
        self.board = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        self.availiable = [1,2,3,4,5,6,7,8,9]
        self.gameEmbed = None
        self.inGame = False


    def charToEmoji(self, char) -> str:
        if char == "X":
            return ":x:"
        elif char == "O":
            return ":o:"
        elif char == "1":
            return ":one:"
        elif char == "2":
            return ":two:"
        elif char == "3":
            return ":three:"
        elif char == "4":
            return ":four:"
        elif char == "5":
            return ":five:"
        elif char == "6":
            return ":six:"
        elif char == "7":
            return ":seven:"
        elif char == "8":
            return ":eight:"
        elif char == "9":
            return ":nine:"

    def boardToEmbed(self) -> Embed:
        strBoard  = f"{self.charToEmoji(self.board[0][0])}<:linevertical:767284991691980811>{self.charToEmoji(self.board[0][1])}<:linevertical:767284991691980811>{self.charToEmoji(self.board[0][2])}\n"
        strBoard += f"<:linehorizontal:767284977838325766><:plus:767285003167203388><:linehorizontal:767284977838325766><:plus:767285003167203388><:linehorizontal:767284977838325766>\n"
        strBoard += f"{self.charToEmoji(self.board[1][0])}<:linevertical:767284991691980811>{self.charToEmoji(self.board[1][1])}<:linevertical:767284991691980811>{self.charToEmoji(self.board[1][2])}\n"
        strBoard += f"<:linehorizontal:767284977838325766><:plus:767285003167203388><:linehorizontal:767284977838325766><:plus:767285003167203388><:linehorizontal:767284977838325766>\n"
        strBoard += f"{self.charToEmoji(self.board[2][0])}<:linevertical:767284991691980811>{self.charToEmoji(self.board[2][1])}<:linevertical:767284991691980811>{self.charToEmoji(self.board[2][2])}\n"

        embed = Embed(description=strBoard)
        embed.set_footer(text=f"Current Player: {self.curPlayer}")

        return embed

    def editBoard(self, spot: int):
        if spot in self.availiable:
            self.availiable.remove(spot)
        x = (spot - 1) // 3
        y = (spot - 1) % 3
        self.board[x][y] = self.curPlayer
        self.switchPlayer()

    def switchPlayer(self):
        if self.curPlayer == 'X':
            self.curPlayer = 'O'
        elif self.curPlayer == 'O':
            self.curPlayer = 'X'

    # ✅ 🚫 ❌ 🛑 ⛔
    @command()
    async def duel(self, ctx: Context, *, target: Optional[Member]):
        if target is not None and target.bot == False:
            msg: Message = await ctx.send(f"{target.mention} hath been challenged to a duel shall thou accept?")

            await msg.add_reaction("✅")
            await msg.add_reaction("❌")

            
            async def waitForConfirmation():
                _reaction = "reaction"
                _user = "user"
                try:
                    _reaction, _user = await self.bot.wait_for("reaction_add")
                    if _user.bot == True:
                        raise ReactorIsBot
                except ReactorIsBot:
                    await waitForConfirmation()
                else:
                    return _reaction, _user


            reaction, user = await waitForConfirmation()

            
            
            if user == target:
                await ctx.send("same person")
                if reaction.emoji == "✅":
                    await ctx.send("thy hast accepted")
                else:
                    await ctx.send("thy hast denied")
            else:
                await ctx.send(f"target: {target}")
                await ctx.send(f"user: {user}")

        else:
            await ctx.send("Invalid target")
        

        

    @command()
    async def newgame(self, ctx: Context):
        if self.inGame == False:

            self.inGame = True

            self.gameEmbed: Message = await ctx.send(embed=self.boardToEmbed())

            await self.gameEmbed.add_reaction("1️⃣")
            await self.gameEmbed.add_reaction("2️⃣")
            await self.gameEmbed.add_reaction("3️⃣")
            await self.gameEmbed.add_reaction("4️⃣")
            await self.gameEmbed.add_reaction("5️⃣")
            await self.gameEmbed.add_reaction("6️⃣")
            await self.gameEmbed.add_reaction("7️⃣")
            await self.gameEmbed.add_reaction("8️⃣")
            await self.gameEmbed.add_reaction("9️⃣")

            await self.waitForReaction()


    async def waitForReaction(self):
        reaction, user = await self.bot.wait_for("reaction_add")

        if (user.bot == False):
            await self.gameEmbed.clear_reaction(reaction.emoji)
            self.editBoard(emojiToNum[reaction.emoji])
            await self.gameEmbed.edit(embed=self.boardToEmbed())
            

        await self.waitForReaction()

    





def setup(bot):
    bot.add_cog(TicTacToe(bot))