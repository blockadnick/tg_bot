import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
def logger(update: Update) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username or update.message.from_user.first_name
    command = update.message.text
    print(f"User {username} (ID: {user_id}) entered command: {command}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger(update)  
    await update.message.reply_text("Hello! I am your bot. How can I help you?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger(update)  
    help_text = (
        "Hello! Here are some commands you can use:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/info - Get more information\n"
    )
    await update.message.reply_text(help_text)

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger(update)
    await update.message.reply_text("This bot was created to help you with basic commands!")


app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("info", info_command))

app.run_polling()
