def class_period():
  time_intervals = []
  # time_intervals = {}
  hour = 8

  # while hour less than latest class hour that is 6 in the evening
  while hour < 18:

      start_time = f"{hour}:00 Hours"
      end_time = f"{hour + 1}:00 Hours"
      formatted_time_interval = (f"{start_time} - {end_time}")
      time_intervals.append(formatted_time_interval)
      hour += 1

  return time_intervals




def class_time_periods():
  """Displays a menu of class periods."""

  print("Welcome to class periods menu.")
  print("Class Period Chart")
  print('                                            ')


  print("1. 8:00 Hours - 9:00 Hours")
  print("2. 9:00 Hours - 10:00 Hours")
  print("3. 10:00 Hours - 11:00 Hours")
  print("4. 11:00 Hours - 12:00 Hours")
  print("5. 12:00 Hours - 13:00 Hours")
  print("6. 13:00 Hours - 14:00 Hours")
  print("7. 14:00 Hours - 15:00 Hours")
  print("8. 5:00 Hours - 16:00 Hours")
  print("9. 16:00 Hours - 17:00 Hours")
  print("10. 17:00 Hours - 18:00 Hours")


  print('                                            ')

  time_intervals = class_period()

  class_period_time = int(input("Enter your Class Period: "))
  time = time_intervals[class_period_time -1]

  return time






