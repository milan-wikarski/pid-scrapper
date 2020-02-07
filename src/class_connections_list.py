import json
import re
from class_connection_detail import ConnectionDetail
from module_request_builder import request_builder


detailLinksRegex = re.compile("data-share-url=\"(.+?)\"")


class ConnectionsList:
  def __init__(self, f, t):
    self.f = f
    self.t = t

    self.connections = []

  def fetch_list(self):
    # Build and send request
    request = request_builder.create().setParam("from", self.f).setParam(
        "to", self.t).build().send()

    # Get detail links and create ConnectionDetail objects
    for link in re.findall(detailLinksRegex, request.html):
      self.connections.append(ConnectionDetail(link, self.f, self.t))

    return self

  def fetch_details(self):
    # Fetch details of all connections
    for connection in self.connections:
      connection.fetch()

    return self
