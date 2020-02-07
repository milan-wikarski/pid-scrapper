text = "\n".join([
    "/start            Starts the bot",
    "/help             Displays list of commands",
    "/routes         Display list of routes",
    "/search         Start a search dialog"
])


def cmd_help(update, context):
  context.bot.send_message(
      chat_id=update.effective_chat.id, text=text)
