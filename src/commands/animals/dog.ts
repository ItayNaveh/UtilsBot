import { CommandOptions, CommandGenerator } from "eris";
import fetch from "node-fetch";


export const name = "dog";

export const settings: CommandOptions = {
	aliases: ["doggo"],
	description: "send a dog",
	fullDescription: "send a doggo, type `.doggo help` for more information",
};

export const exec: CommandGenerator = async(msg, args) => {
	if (args.length > 0 && args[0] == "help") {
		return { embed: {
			title: "Help For Doggos",
			fields: [
				{ name: "As far as i know there are no options", value: "boop" }
			],
			footer: {
				text: "Doggos By https://thedogapi.com/ \nfor more information got to the link above"
			}
		} };
	} else {
		const response = await fetch("https://api.thedogapi.com/v1/images/search");
		const data = await response.json();
		(await msg.channel.createMessage(data[0].url)).addReaction("🐶");
	}
};
