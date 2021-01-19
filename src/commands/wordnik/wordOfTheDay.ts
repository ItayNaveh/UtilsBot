import { CommandOptions, CommandGenerator } from "eris";
import fetch from "node-fetch";


export const name = "wordoftheday";

export const settings: CommandOptions = {
	caseInsensitive: true,
	aliases: ["word-of-the-day"],
	description: "sends the word of the day",
	fullDescription: "sends the word of the day",
};

export const exec: CommandGenerator = async(msg, args) => {
	const response = await fetch(`https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=${process.env.WORDNIK_API_KEY}`);
	const data = await response.json();
	const word = data.word;
	msg.channel.createMessage(`word of the day: ${word}`);
	const definitions = data.definitions;
	for (let i = 0; i < definitions.length; i++) {
		msg.channel.createMessage(`definition ${i+1}: ${definitions[i].text}`);
	}
};
