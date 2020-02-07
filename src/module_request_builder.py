import requests
import bs4


class Request:
  def __init__(self, base):
    self.base = base

    self.params = {
        "to": None,
        "from": None
    }

    self.url = None

    self.html = None

  def setParam(self, param, value):
    if (param == "from"):
      self.params["from"] = value
    elif (param == "to"):
      self.params["to"] = value

    return self

  def build(self):
    res = self.base
    args = []

    if (self.params["from"] is not None):
      args.append("f=" + self.params["from"])

    if (self.params["to"] is not None):
      args.append("t=" + self.params["to"])

    if (len(args) > 0):
      res += "?" + "&".join(args)

    self.url = res

    return self

  def send(self):
    self.html = str(bs4.BeautifulSoup(
        requests.get(self.url).text, "html.parser"))

    return self


class RequestBuilder:
  def __init__(self):
    pass

  def create(self, base="https://idos.idnes.cz/pid/spojeni/vysledky/"):
    return Request(base)


request_builder = RequestBuilder()
