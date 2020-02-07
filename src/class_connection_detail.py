import json
import re
from module_request_builder import request_builder
from class_day_time import DayTime
from class_time_location import TimeLocation


dateRegex = re.compile(
    "<h2 class=\"reset date\">(\d{1,2}:\d{1,2})<span class=\"date-after\">(.+?)</span>"
)
partsNameRegex = re.compile("(Tram \d+|Metro [ABC]|Bus \d+)")
partsTimeRegex = re.compile("<p class=\"reset time\">(\d{1,2}:\d{1,2})</p>")
partsLocationRegex = re.compile("<strong class=\"name\">(.+?)</strong>")


class ConnectionDetailPart:
  def __init__(self, route, arrival: TimeLocation, departure: TimeLocation):
    self.route = route
    self.arrival = arrival
    self.departure = departure


class ConnectionDetail:
  def __init__(self, link, f, t):
    self.link = link

    self.f = f
    self.t = t

    self.parts = []

    self.date = None
    self.time = None

    self.departure_time = None
    self.arrival_time = None

    self.duration = None

  def fetch(self):
    # Build and send request
    request = request_builder.create(self.link).build().send()

    # Parse date and time
    datetime = list(reversed(list(re.findall(dateRegex, request.html)[0])))
    self.date = datetime[0]
    self.time = DayTime(datetime[1])

    # Parse parts
    parts_names = re.findall(partsNameRegex, request.html)
    parts_times = re.findall(partsTimeRegex, request.html)
    parts_locations = re.findall(partsLocationRegex, request.html)

    for i in range(len(parts_names)):
      route = parts_names[i]
      departure = TimeLocation(parts_times[i * 2], parts_locations[i * 2])
      arrival = TimeLocation(
          parts_times[i * 2 + 1], parts_locations[i * 2 + 1])

      self.parts.append(ConnectionDetailPart(route, arrival, departure))

    # Departure and Arrival time
    self.departure_time = self.parts[0].departure.time
    self.arrival_time = self.parts[len(self.parts) - 1].arrival.time

    # Duration
    self.duration = DayTime.compare(self.departure_time, self.arrival_time)

  def pretty_print(self):
    routes_header = []

    for part in self.parts:
      routes_header.append(part.route)

    res = []
    res.append(" --> ".join(routes_header))
    res.append("{0} --> {1}, *{2} minutes*\n".format(self.departure_time,
                                                     self.arrival_time, self.duration))

    for part in self.parts:
      res.append("*{0}*\n  {1}      {2}\n  {3}      {4}".format(part.route, part.departure.time,
                                                                part.departure.location, part.arrival.time, part.arrival.location))
    return "\n".join(res)
