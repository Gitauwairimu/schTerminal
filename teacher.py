def teacher_menu():
  """Displays the teachers menu and allows the user to select an option."""

  print("1. Attendance")
  print("2. Post Exam Results")
  print("3. Post Class Schedule")
  print("4. View Students")
  print("5. Issue Homework")
  print("6. Back")

  print('............................................')
  print('                                            ')
  print('                                            ')

  choice = input("Enter your choice: ")

  if choice == "1":
    attendance_menu() 
  elif choice == "2":
    post_exam_results()
  elif choice == "3":
    post_class_schedule()
  elif choice == "4":
    view_all_students()
  elif choice == "5":
    issue_homework()
  elif choice == "6":
    teacher_menu()
  else:
    print("Invalid choice")
    teacher_menu()

 # view and create functions

def post_class_schedule():
  """Allows the teacher to post the class schedule."""
  
  # Get a list of all the lecture halls.
  lecture_halls = get_lecture_halls()

  # Prompt the teacher to choose a lecture hall.
  print("Select a lecture hall:")
  for index, lecture_hall in enumerate(lecture_halls):
    print(f"{index + 1}. {lecture_hall}")
  choice = input("Choose Lecture Hall: ")

  # Validate the input.
  if choice not in range(1, len(lecture_halls) + 1):
    raise ValueError("Invalid choice")

  # Get the selected lecture hall.
  location = lecture_halls[choice - 1]

  print("Enter the class name: ")
  class_name = input()

  print("Enter the start date: ")
  start_date = input()

  print("Enter the end date: ")
  end_date = input()

  print("Enter the time: ")
  time = input()

  print("Enter the location: ")
  location = input()

  # Post the class schedule to the database.

def get_lecture_halls():
  """Gets a list of all the lecture halls from the database."""

  # Connect to the database.
  connection = connect_to_database()

  # Get a cursor.
  cursor = connection.cursor()

  # Execute the query.
  cursor.execute("SELECT * FROM lecture_halls")

  # Get the results.
  lecture_halls = cursor.fetchall()

  # Close the connection.
  connection.close()

  # Return the list of lecture halls.
  return lecture_halls


def attendance_menu():
  """Displays the attendance menu and allows the teacher to select an option."""

  print("1. Take Daily Attendance")
  print("2. View Attendance")
  print("3. Update Attendance")
  print("4. Back")

  print('............................................')
  print('                                            ')
  print('                                            ')

  choice = input("Enter your choice: ")

  if choice == "1":
    take_daily_attendance()
  elif choice == "2":
    view_attendance()
  elif choice == "3":
    update_attendance()
  elif choice == "4":
    attendance_menu()
  else:
    print("Invalid choice")
    attendance_menu()
