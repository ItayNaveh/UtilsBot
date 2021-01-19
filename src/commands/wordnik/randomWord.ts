import { CommandOptions, CommandGenerator, CommandGeneratorFunction } from "eris";
import fetch from "node-fetch";


export const name = "randomword";

export const settings: CommandOptions = {
	caseInsensitive: true,
	aliases: ["random-word"],
	description: "sends a random word",
	fullDescription: "sends a random word",
};

export const exec: CommandGenerator = async(msg, args) => {
	const randomWord = await fetch(`https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&api_key=${process.env.WORDNIK_API_KEY}`);
	const data = await randomWord.json();
	const word = data.word;
	msg.channel.createMessage(word);

	const response = await fetch(`https://api.wordnik.com/v4/word.json/${word}/definitions?limit=3&includeRelated=false&sourceDictionaries=all&useCanonical=false&includeTags=false&api_key=${process.env.WORDNIK_API_KEY}`);
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
};
