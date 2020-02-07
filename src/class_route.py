class Route:
  def __init__(self, name, desc, type):
    self.type = type.capitalize()
    self.id = self.type + " " + name
    self.route = desc

  def __str__(self):
    return '{ "type": "{0}", "id": "{1}", "route": "{2}" }'.format(self.type, self.id, self.route)
