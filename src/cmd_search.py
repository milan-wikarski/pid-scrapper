from module_state import state
from class_search_query import SearchQuery


def cmd_search(update, context):
  user = update.effective_chat.id

  # Reset search params
  state.search[user] = SearchQuery()

  context.bot.send_message(
      chat_id=user, text="Okay, I will help you find the route.\nHow about you start by telling me where you are?")
