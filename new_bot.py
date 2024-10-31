import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from get_quotes import get_quotes

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
def logger_info_for_admin(update: Update) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username or update.message.from_user.first_name
    command = update.message.text
    print(f"User {username} (ID: {user_id}) entered command: {command}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger_info_for_admin(update)  
    await update.message.reply_text("Hello! I am your bot. How can I help you?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger_info_for_admin(update)  
    help_text = (
        "Hello! Here are some commands you can use:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/info - Get current price\n"
    )
    await update.message.reply_text(help_text)

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Enter a symbol to get current price:")
    context.user_data['awaiting_symbol'] = True

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.user_data.get('awaiting_symbol'):
        symbol = update.message.text
        price_info = get_quotes(symbol)
        await update.message.reply_text(price_info)
        context.user_data['awaiting_symbol'] = False

app = ApplicationBuilder().token(bot_token).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("info", info_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
