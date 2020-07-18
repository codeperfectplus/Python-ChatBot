from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

BOTNAME = "Jarvis"

def start():
	bot = ChatBot(BOTNAME,
		logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90,
        },        
    ],
		preprocessors = [
			"chatterbot.preprocessors.clean_whitespace",
		],
		input_adaptor="chatterbot.input.TerminalAdaptor",
        output_adaptor="chatterbot.output.TerminalAdaptor",
		database_uri='sqlite:///database.sqlite3')

	trainer = ChatterBotCorpusTrainer(bot)

	# Train based on the english corpus
	trainer.train(
		"chatterbot.corpus.english",
		"chatterbot.corpus.english.greetings",
		"chatterbot.corpus.english.conversations",
		)


	print(f"Hello I am {BOTNAME}")

	while True:
		try:
			bot_input = input("You: ")
			bot_respose = bot.get_response(bot_input)
			print(f"{BOTNAME}: {bot_respose}")

		except(KeyboardInterrupt, EOFError, SystemExit):
			break

if __name__ == "__main__":
	start()