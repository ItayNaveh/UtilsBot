import os
from bot.bot import UtilsBot


def main():
	bot = UtilsBot(".")
	try:
		token = os.environ["BOT_TOKEN"]
		bot.run(token)
	except KeyError:
		from dotenv import load_dotenv
		load_dotenv()
		token = os.environ["BOT_TOKEN"]
		bot.run(token)


if __name__ == "__main__":
	main()
