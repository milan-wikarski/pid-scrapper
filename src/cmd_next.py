from module_state import state


def cmd_next(update, context):
  user = update.effective_chat.id

  if (user not in state.search):
    return context.bot.send_message(
        chat_id=user, text="You haven't searched for a connection yet. Use /search to do so")

  state.search[user].next_connection()

  context.bot.send_message(
      chat_id=user, text=state.search[user].current_message, parse_mode="markdown")
