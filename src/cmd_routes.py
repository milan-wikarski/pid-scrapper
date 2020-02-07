from module_routes_manager import routes_manager

response = "\n".join([
    "Please, specify the type of routes you want to display:",
    "/routes_tram for tram routes",
    "/routes_bus for bus routes",
    "/routes_metro for metro routes",
    "/routes_train for train routes"
])


def cmd_routes(update, context):
  return context.bot.send_message(
      chat_id=update.effective_chat.id, text=response)


def cmd_routes_type(update, context, type):
  page = 1

  if (len(context.args) >= 1 and str(context.args[0]).isnumeric()):
    page = int(context.args[0])

  return context.bot.send_message(
      chat_id=update.effective_chat.id, text=routes_manager.print_routes_by_type(type, page), parse_mode="markdown")


def cmd_routes_bus(update, context):
  return cmd_routes_type(update, context, "Bus")


def cmd_routes_tram(update, context):
  return cmd_routes_type(update, context, "Tram")


def cmd_routes_metro(update, context):
  return cmd_routes_type(update, context, "Metro")


def cmd_routes_train(update, context):
  return cmd_routes_type(update, context, "Train")
