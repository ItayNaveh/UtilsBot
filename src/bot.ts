import { readdir } from "fs/promises";
import { CommandClient } from "eris";

const bot = new CommandClient(process.env.BOT_TOKEN, {}, {
	owner: "Itay",
	prefix: ".",
});

bot.on("ready", () => {
	console.log("Bot's Ready");
});

(async() => {
	const commands = await readdir("build/commands");
	for (const commandFile of commands) {
		const command = await import(`./commands/${commandFile}`);
		bot.registerCommand(command.name, command.exec, command.settings);
	}
})().then(() => {
	bot.connect();
});
