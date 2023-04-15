import telegram
from telegram import Bot, _update
from telegram.ext import _commandHandler, _updater, _messageHandler, filters
import openai
import os
#CommandHandler, Dispatcher, MessageHandler, Filters

# Initialize the OpenAI API key
openai.api_key = os.environ["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"]

# Define a function to generate a response using ChatGPT
def generate_response(text):
    prompt = f"Conversation with a user:\n\nUser: {text}\nAI:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text.strip()
    return response

# Define a function to handle incoming messages from the Telegram bot
def handle_message(update, context):
    text = update.message.text
    response = generate_response(text)
    update.message.reply_text(response)

# Initialize the Telegram bot and connect it to the chatGPT model
updater = Updater(token="5829477521:AAH6_LfvVCpUDQBHBpZ6uzOwiIfQXYmOLvQ", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

# Start the bot
updater.start_polling()

#from telegram.ext.filters import Filters

# ...

#dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))
