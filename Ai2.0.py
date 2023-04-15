import os
import telegram
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Set up Telegram bot token
bot = telegram.Bot(token="5829477521:AAH6_LfvVCpUDQBHBpZ6uzOwiIfQXYmOLvQ")

# Define function to handle incoming messages
def handle_message(update, context):
    # Get message text and chat ID
    message = update.message.text
    chat_id = update.message.chat_id
    
    # Call OpenAI GPT-3 API to generate response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        temperature=0.5,
        max_tokens=50,
        n=1,
        stop=None,
        timeout=10,
    )
    reply = response.choices[0].text.strip()
    
    # Send response back to Telegram chat
    bot.send_message(chat_id=chat_id, text=reply)

# Set up handler for incoming messages
updater = telegram.ext.Updater(token="<YOUR_TELEGRAM_BOT_TOKEN>", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

# Start the bot
updater.start_polling()
updater.idle()
