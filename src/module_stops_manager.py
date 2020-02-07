import json


class StopsManager:
  def __init__(self):
    self.stops = set()

    with open("src/data/stops.json", "r") as f:
      for stop in json.loads(f.read()):
        self.stops.add(stop["name"])


stops_manager = StopsManager()
