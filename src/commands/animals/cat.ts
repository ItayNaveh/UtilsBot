import { CommandOptions, CommandGenerator, MessageFile } from "eris";
import fetch from "node-fetch";


export const name = "cat";

export const settings: CommandOptions = {
	description: "a cute cat",
	fullDescription: "a very cute cat, type `.cat help` for options",
};

const getCat = async(url: string, name: string): Promise<MessageFile> => {
	const response = await fetch(url);
	const image = await response.buffer();
	return {
		name: name,
		file: image
	};
};

export const exec: CommandGenerator = async(msg, args) => {
	if (args.length > 0) {
		if (args[0] == "help") {
			return { embed: {
				title: "Help For Cats",
				description: "{ -- } means you need to put yourself a value",
				fields: [
					{ name: "{tag}", value: "A cat with a tag" },
					{ name: "gif", value: "A cat gif" },
					{ name: "says {text}", value: "A cat saying text" },
					{ name: "{tag} says {text}", value: "A cat with a tag saying text" },
				],
				footer: {
					text: "Cats By: https://cataas.com/ \nfor more options go to the link above"
				},
			} };
		}

		const things = args.join("/");
		if (args[0] == "gif") {
			const cat = await getCat(`https://cataas.com/cat/${things}`, "cat.gif");
			await (await msg.channel.createMessage("", cat)).addReaction("🐱");
		} else {
			const cat = await getCat(`https://cataas.com/cat/${things}`, "cat.jpg");
			await (await msg.channel.createMessage("", cat)).addReaction("🐱");
		}
	} else {
		const cat = await getCat("https://cataas.com/cat", "cat.jpg");
		await (await msg.channel.createMessage("", cat)).addReaction("🐱");
	}
};
