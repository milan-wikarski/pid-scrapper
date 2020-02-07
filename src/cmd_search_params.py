from module_state import state
from class_connections_list import ConnectionsList
from module_stops_manager import stops_manager


def cmd_search_params(update, context):
  user = update.effective_chat.id

  if (user not in state.search):
    return

  text = update.effective_message.text

  if (text not in stops_manager.stops):
    return context.bot.send_message(
        chat_id=user, text="I am sorry, but I haven't found stop called *{0}*. Maybe you made a mistake? Try it again.".format(text), parse_mode="markdown")
  # Setting <from>
  if (state.search[user].f is None):
    state.search[user].f = text

    context.bot.send_message(
        chat_id=user, text="Okay, I am looking for connections from *{0}*.\nNow tell me where you want to go.".format(text), parse_mode="markdown")

  # Setting <to>
  elif (state.search[user].t is None):
    state.search[user].t = text

    f = state.search[user].f
    t = state.search[user].t

    context.bot.send_message(
        chat_id=user, text="Looking for connections from *{0}* to *{1}*...".format(f, t), parse_mode="markdown")

    state.search[user].fetch_connections()
    state.search[user].next_connection()

    context.bot.send_message(
        chat_id=user, text=state.search[user].current_message, parse_mode="markdown")
