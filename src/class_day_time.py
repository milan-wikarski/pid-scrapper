class DayTime:
  # Expects time in format HH:MM
  def __init__(self, time):
    self.time = time
    self.parts = list(map(int, time.split(":")))
    self.minutes = self.parts[0] * 60 + self.parts[1]

  def __str__(self):
    return self.time

  @staticmethod
  def compare(start, end):
    start_minutes = start.minutes
    end_minutes = end.minutes

    # Correction in case of day overlap
    if (end_minutes < start_minutes):
      end_minutes += 1440

    return end_minutes - start_minutes
