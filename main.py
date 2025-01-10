from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from anagram import Anagram
from station_scraper import StationScraper

from datetime import datetime

scraper = StationScraper()

anagram = Anagram(scraper.getNames())

TOKEN = open("token.txt", "r").readline()
BOT_Username = "TODO"

def log(txt):
    with open("log.txt", 'a') as f:
        f.write(f"{datetime.now()}: {txt}\n")

# Commands
async def start_command(update, context):
    log(f"Update: {update}")
    await update.message.reply_text("Hallo, stuur een berichtje met de"\
                                    "gehusselde letters van een stationsnaam"\
                                    "zoals in de NS puzzels en je krijgt het"\
                                    "juiste station terug")

# Messages
async def handle_message(update, context):
    log(f"Update: {update}")
    text = anagram.getAnagram(update.message.text)
    if not text:
        text = "Voor deze input heb ik geen station kunnen vinden, weet je"\
                "zeker dat je het correct hebt getypt?"
    
    await update.message.reply_text(text)

# Errors
async def handle_error(update, context):
    log(f"Update: {update}")
    print(f"Update: {update}, caused error: {context.error}")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    # Command Handlers
    app.add_handler(CommandHandler("start", start_command))

    # Message Handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(handle_error)

    # Settings
    app.run_polling(poll_interval=1)
