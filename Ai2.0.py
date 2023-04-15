import os
import telegram
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Initialize Telegram bot and OpenAI API
telegram_bot_token = os.environ.get('5829477521:AAH6_LfvVCpUDQBHBpZ6uzOwiIfQXYmOLvQ')
openai_api_key = os.environ.get('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')
bot = telegram.Bot(token=telegram_bot_token)
openai.api_key = openai_api_key

# Define message handlers
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a bot Created by @Anonymous728. Send me a message and I'll respond with something smart!")

def reply_to_message(update, context):
    message = update.message.text
    response = openai.Completion.create(engine="davinci", prompt=message, max_tokens=50).choices[0].text
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Create the updater and add handlers
updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_to_message))

# Start the bot
updater.start_polling()
updater.idle()
