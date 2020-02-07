import json
from class_route import Route
from math import ceil


class RoutesManager:
  def __init__(self):
    self.routes = []

    with open("src/data/routes.json", "r") as f:
      for route in json.loads(f.read()):
        self.routes.append(Route(route["name"], route["desc"], route["type"]))

    self.routes_by_type = {}

  def get_routes_by_type(self, type):
    if (type not in self.routes_by_type):
      self.routes_by_type[type] = []

      for route in self.routes:
        if (route.type == type):
          self.routes_by_type[type].append(route)

    return self.routes_by_type[type]

  def print_routes_by_type(self, type, page=1):
    STEP = 10

    routes = self.get_routes_by_type(type)

    max_page = ceil(len(routes) / STEP)
    page = min(page, max_page)

    start = (page - 1) * STEP
    end = min(start + STEP, len(routes))

    res = [
        "Displaying routes of type {0}".format(type),
        "Page {0} of {1} ({2}-{3})\n".format(page, max_page, start + 1, end)]

    for i in range(start, end):
      route = routes[i]
      res.append("*{0}*: {1}".format(route.id, route.route))

    res.append(
        "\nUse `/routes_{0} $1` where $1 is page number".format(type.lower()))

    return "\n".join(res)


routes_manager = RoutesManager()
