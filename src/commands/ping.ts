import { CommandOptions, CommandGenerator } from "eris";


export const name = "ping";

export const settings: CommandOptions = {
	description: "pong",
	fullDescription: "to test if the bot works",
};

export const exec: CommandGenerator = (msg, args) => {
	return "pong";
};