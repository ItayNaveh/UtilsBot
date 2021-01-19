import { CommandOptions, CommandGenerator } from "eris";
import fetch from "node-fetch";

export const name = "define";

export const settings: CommandOptions = {
	description: "shows a definition of a word",
	fullDescription: "shows a definition of a word",
	usage: "<word>",
};

export const exec: CommandGenerator = async(msg, args) => {
	if (args.length > 0) {
		const response = await fetch(`https://api.wordnik.com/v4/word.json/${args[0]}/definitions?limit=3&includeRelated=false&sourceDictionaries=all&useCanonical=false&includeTags=false&api_key=${process.env.WORDNIK_API_KEY}`);
		const definitions = await response.json();
		if (Array.isArray(definitions)) {
			for (const definition of definitions) {
				const txt: string = definition.text.replace(/<em>|<\/em>/g, "*");
				const partOfSpeech = definition.partOfSpeech;
				msg.channel.createMessage(`definition: **${partOfSpeech}** ${txt}`);
			}
		} else {
			return "No Definitions Found";
		}
	} else {
		return "Invalid Input";
	}
};
