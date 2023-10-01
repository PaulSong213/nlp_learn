from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

bot = ChatBot(
    'Norman',
    read_only=True,
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'trainers.correct_zarate'
    ],
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.80
        }
    ]
)

# Train the bot
# corpus_trainer = ChatterBotCorpusTrainer(bot)

# corpus_trainer.train(
#     "chatterbot.corpus.english.greetings",
#     "chatterbot.corpus.english.conversations",
#     "chatterbot.corpus.english.health",
# )

list_trainer = ListTrainer(bot)
list_trainer.train([
    'Where is the address E. Zarate Hospital?',
    'E. Zarate Hospital is located at 16 J. Aguilar Avenue, Talon Uno, Las Piñas City',
])

list_trainer.train([
    'What are the patients visiting hours?',
    'Visiting hours are typically from 9AM to 10PM every day.',
])

# Make the bot respond in the command line
while True:
    try:
        user_input = input()
        bot_input = bot.get_response(user_input)
        print(bot_input)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
