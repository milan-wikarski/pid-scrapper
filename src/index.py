import logging
import os
import json

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

from cmd_help import cmd_help
from cmd_start import cmd_start
from cmd_routes import cmd_routes, cmd_routes_bus, cmd_routes_metro, cmd_routes_train, cmd_routes_tram
from cmd_search import cmd_search
from cmd_search_params import cmd_search_params
from cmd_next import cmd_next


# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


# Load .env
load_dotenv()


# Telegram bot
updater = Updater(token=os.getenv("TELEGRAM_TOKEN"), use_context=True)
dispatcher = updater.dispatcher


# Commands
dispatcher.add_handler(CommandHandler("start", cmd_start))
dispatcher.add_handler(CommandHandler("help", cmd_help))

dispatcher.add_handler(CommandHandler("routes", cmd_routes))
dispatcher.add_handler(CommandHandler("routes_bus", cmd_routes_bus))
dispatcher.add_handler(CommandHandler("routes_metro", cmd_routes_metro))
dispatcher.add_handler(CommandHandler("routes_tram", cmd_routes_tram))
dispatcher.add_handler(CommandHandler("routes_train", cmd_routes_train))

dispatcher.add_handler(CommandHandler("search", cmd_search))
dispatcher.add_handler(CommandHandler("next", cmd_next))
dispatcher.add_handler(MessageHandler(Filters.text, cmd_search_params))

# Run app
updater.start_polling()
print("The bot is running...")
