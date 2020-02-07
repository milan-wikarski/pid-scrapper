from class_connections_list import ConnectionsList


class SearchQuery:
  def __init__(self, f=None, t=None):
    self.f = f
    self.t = t

    self.next = 0
    self.connections = []
    self.current_message = ""

  def fetch_connections(self):
    self.connections = ConnectionsList(self.f, self.t).fetch_list().connections

  def next_connection(self):
    if (len(self.connections) == 0):
      self.current_message = "No connections were found"
      return False

    if (self.next >= len(self.connections)):
      self.current_message = "I am sorry, but I only have {0} connection(s)".format(
          len(self.connections))
      return False

    connection = self.connections[self.next]
    connection.fetch()

    self.next += 1

    self.current_message = connection.pretty_print()
    self.current_message += "\n\nTo display next connection use /next"

    return True
