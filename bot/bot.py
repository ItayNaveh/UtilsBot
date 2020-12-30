from pathlib import Path

from discord.ext.commands import Bot, Context


class UtilsBot(Bot):
	def __init__(self, prefix):
		self._cogs = [p.stem for p in Path(".").glob("./bot/cogs/*.py")]
		super().__init__(command_prefix=prefix)

	def setup(self):
		print("Running setup...")
		for cog in self._cogs:
			self.load_extension(f"bot.cogs.{cog}")
			print(f"\tLoaded `{cog}` cog")

		print("Finished setup")

	def run(self, token):
		self.setup()
		super().run(token)

	async def on_ready(self):
		print("Bot's ready")
