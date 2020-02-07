from class_day_time import DayTime


class TimeLocation:
  def __init__(self, time, location):
    self.time = DayTime(time)
    self.location = location
