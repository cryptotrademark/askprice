from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ⚠️ WARNING: Your token is hardcoded here for immediate testing. 
# DO NOT commit this file to GitHub or share it. 
# In a real application, use environment variables.
TOKEN = '8919169222:AAFx5hOU0pgx-HBFMcJCVB8nwl3ddVUl2k8'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    await update.message.reply_text("Hello! 👋 How can I assist you today?")

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Check if the message is 'hi' or 'hello' and reply accordingly."""
    
    user_text = update.message.text.lower().strip()
    
    if user_text in ['hi', 'hello']:
        await update.message.reply_text("Hello! 👋 I am a test bot. How can I help you?")
    else:
        await update.message.reply_text("I only understand 'hi' or 'hello' right now! \n\nType /start to see my welcome message.")

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # 1. Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # 2. Register a handler for regular text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))

    # Start the Bot
    print("Bot is running and polling for messages...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()