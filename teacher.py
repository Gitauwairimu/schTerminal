from contdb import connect_to_database
from class_time import class_period, class_time_periods
from attendance import take_daily_attendance, view_attendance, update_attendance
from admin import get_all_data, user
import prettytable
import datetime


def teacher_menu():
  """Displays the teachers menu and allows the user to select an option."""

  print("1. Attendance")
  print("2. Post Exam Results")
  print("3. Post Class Schedule")
  print("4. View Students")
  print("5. Issue Assignment")
  print("6. View All Assignment")
  print("7. Back")

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
    create_assignment()
  elif choice == "6":
    view_all_assignments()
  elif choice == "7":
    teacher_menu()
  else:
    print("Invalid choice")
    teacher_menu()

 # view and create functions

# def post_class_schedule():
#   """Allows the teacher to post the class schedule."""
  
#   # Get a list of all the lecture halls.
#   lecture_halls = get_lecture_halls()

#   # Prompt the teacher to choose a lecture hall.
#   print("Select a lecture hall:")
#   for index, lecture_hall in enumerate(lecture_halls):
#     print(f"{index + 1}. {lecture_hall}")
#   choice = int(input("Choose Lecture Hall: "))

#   # Validate the input.
#   if choice not in range(1, len(lecture_halls) + 1):
#     raise ValueError("Invalid choice")

#   # Get the selected lecture hall.
#   location = (lecture_halls[choice - 1])[0]
#   print(f"You have chosen: {location}")

#   print("Enter the class name: ")
#   class_name = input()

#   print("Enter the class tutor: ")
#   class_tutor = get_all_data()

#   print("Enter days class held: ")
#   class_days = input()

#   print("Enter the start date: ")
#   start_date = input()

#   print("Enter the end date: ")
#   end_date = input()

#   # print("Enter the time: ")
#   # time = input()
#   print("Choose class time from list: ")
#   print('                                 ')
#   print(class_period())
#   print('                                 ')
#   time = class_time_periods()
#   print('                                 ')

def view_all_students():
  """View all students in the database."""

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor to execute SQL statements.
  cursor = connection.cursor()

  # Get all students.
  cursor.execute('SELECT student_adm, first_name, surname, email, role FROM students')
  students = cursor.fetchall()

  # Close the connection to the database.
  connection.close()

  # Create a pretty table.
  table = prettytable.PrettyTable(hide_columns=["password"])

  # Add the headers to the table.
  table.field_names = ["Student ID", "Name", "Role", "Email"]

  # Add the data to the table.
  for student in students:
    table.add_row([student[0], student[1] + ' ' + student[2 ], student[4], student[3]])

  # Print the table.
  print(table)


def post_class_schedule():
  """Allows the teacher to post the class schedule."""

  # Get a list of all the lecture halls.
  lecture_halls = get_lecture_halls()

  # Prompt the teacher to choose a lecture hall.
  print("Select a lecture hall:")
  for index, lecture_hall in enumerate(lecture_halls):
    print(f"{index + 1}. {lecture_hall}")
  choice = int(input("Choose Lecture Hall: "))

  # Validate the input.
  if choice not in range(1, len(lecture_halls) + 1):
    raise ValueError("Invalid choice")

  # Get the selected lecture hall.
  location = (lecture_halls[choice - 1])[0]
  print(f"You have chosen: {location}")

  print("Enter the class name: ")
  class_name = input()

  # Get all teachers from the database.
  teachers = get_all_teachers()

  print("Choose a class tutor from list: ")
  print('                                 ')
  for index, teacher in enumerate(teachers):
    print(f"{index + 1}. {teacher[1]}")
  print('                                 ')
  class_tutor = int(input("Choose Class Tutor: "))

  print("Enter days of week class held: ")
  class_days = input()

  print("Enter the start date: ")
  start_date = input()

  print("Enter the end date: ")
  end_date = input()

  print("Choose class time from list: ")
  print('                                 ')
  print(class_period())
  print('                                 ')
  time = class_time_periods()
  print('                                 ')

  # Get the name of the teacher associated with the integer value of class_tutor.
  class_tutor = teachers[class_tutor - 1][1]

  # Save the data to the database.
  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor to execute SQL statements.
  cursor = connection.cursor()

  # Insert the data into the table.
  # cursor.execute('INSERT INTO class_schedule (class_name, class_tutor, class_days, start_date, end_date, time, location) VALUES (?, ?, ?, ?, ?, ?, ?)',
              # (class_name, class_tutor, class_days, start_date, end_date, time, location))
  # Insert the data into the table.
  # Insert the data into the table.
  cursor.execute('INSERT INTO class_schedule (class_name, class_tutor, class_days, start_date, end_date, time, location) VALUES (%s, %s, %s, %s, %s, %s, %s)',
              (class_name,
               class_tutor,
               class_days,
               start_date,
               end_date,
               time,
               location));
  # Commit the changes to the database.
  connection.commit()

  # Close the connection to the database.
  connection.close()

  print('Class Saved in Database')



# # save data to database

#fetch all below data from database
  # print(f"Class name: {class_name}")
  # # print(f"Lecturer: {class_tutor}")
  # # print(typeof(class_tutor)) 
  # print(f"Location: {location} Hall")
  # print(f"Class Days: Every {class_days} between {time}")
  # print(f"Classes Start: {start_date} and End: {end_date}")
  # print('                                 ')

  # Post the class schedule to the database.

def get_all_teachers():
  """Gets all teachers from the database."""

  # Create a connection to the database.
  connection = connect_to_database()
  # Create a cursor to execute SQL statements.
  cursor = connection.cursor()

  # Fetch all teachers from the database.
  cursor.execute('SELECT * FROM teachers')
  teachers = cursor.fetchall()

  # Close the connection to the database.
  connection.close()

  return teachers

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
    teacher_menu()
  else:
    print("Invalid choice")
    teacher_menu()


def create_assignment():
  """Creates a new assignment."""

  # Get the assignment details from the user.
  print("Enter the assignment name: ")
  assignment_name = input()

  print("Enter the assignment description: ")
  assignment_description = input()

  try:
    print("Enter the due date (YYYY-MM-DD): ")
    due_date = input()

    # Convert the due date to a valid format.
    due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').strftime('%Y-%m-%d')


  except ValueError:
    print("Invalid date format. Please enter the due date in the format YYYY-MM-DD")


  print("Enter the submission instructions: ")
  submission_instructions = input()

  # Get all teachers from the database.
  teachers = get_all_teachers()

  print("Choose Assignment Creator: ")
  print('                                 ')
  for index, teacher in enumerate(teachers):
    print(f"{index + 1}. {teacher[1]}")
  print('                                 ')
  instructor = int(input("Choose Class Tutor: "))

  # Get the list of courses from the database.
  connection = connect_to_database()

  cursor = connection.cursor()

  cursor.execute('SELECT class_name FROM class_schedule')
  courses = cursor.fetchall()

  # Choose a course from the list.
  print("Choose a course:")
  for index, course in enumerate(courses):
    print(f"{index + 1}. {course[0]}")
  choice = int(input("Choose Course: "))

  # Validate the input.
  if choice not in range(1, len(courses) + 1):
    raise ValueError("Invalid choice")

  course = courses[choice - 1][0]

  # Save the assignment details to the database.
  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor to execute SQL statements.
  cursor = connection.cursor()

  # Insert the assignment details.
  cursor.execute('INSERT INTO assignments (assignment_name, assignment_description, due_date, submission_instructions, instructor, course) VALUES (%s, %s, %s, %s, %s, %s)',
              (assignment_name, assignment_description, due_date, submission_instructions, instructor, course))

  # Commit the changes to the database.
  connection.commit()

  # Close the connection to the database.
  connection.close()

  print('Assignment Created')


def view_all_assignments():
  """Sees all the assignments in the database."""

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor to execute SQL statements.
  cursor = connection.cursor()

  # Get all the assignments.
  cursor.execute('SELECT * FROM assignments')
  assignments = cursor.fetchall()

  # Print the assignments.
  for assignment in assignments:
    print('                                ')
    print(f"Assignment Name: {assignment[1]}")
    print(f"Course Name: {assignment[6]}")
    print(f"Instructor Name: {assignment[5]}")
    print(f"Due Date: {assignment[3]}")
    print('                                ')
    print(f"Assignment Description: {assignment[2]}")
    print('                                ')
    print('                                ')
    print(f"Submission Instructions: {assignment[4]}")
    print('                                ')
    print('...........................................')
    
  
  # Close the connection to the database.
  connection.close()

def post_exam_results():
  """Posts the exam results to the database."""

  # Get the exam name from the user.
  print("Enter the exam type: ")
  exam_name = input()

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor to execute SQL statements.
  cursor = connection.cursor()

  # Get all the courses from the database.
  cursor.execute('SELECT class_name FROM class_schedule')
  courses = cursor.fetchall()

  # Prompt the user to choose a course.
    # Choose a course from the list.
  print("Choose a course:")
  for index, course in enumerate(courses):
    print(f"{index + 1}. {course[0]}")
  choice = int(input("Choose Course: "))

  # Validate the input.
  if choice not in range(1, len(courses) + 1):
    raise ValueError("Invalid choice")
  
  course_name = courses[choice - 1][0]

  # Get the class tutor associated with the course.
  cursor.execute('SELECT class_tutor FROM class_schedule WHERE class_name = %s', (course_name,))
  class_tutor = cursor.fetchone()[0]

  print(class_tutor)


  # Get the student ID from the user.
  print("Enter the student ID: ")
  student_id = input()

  # # Get the date exam taken from the user.
  # print("Enter the student ID: ")
  # date_taken = input()

  try:
    print("Enter date exam taken (YYYY-MM-DD): ")
    date_taken = input()

    # Convert the due date to a valid format.
    date_taken = datetime.datetime.strptime(date_taken, '%Y-%m-%d').strftime('%Y-%m-%d')

  except ValueError:
    print("Invalid date format. Please enter the due date in the format YYYY-MM-DD")

  # Get the exam score from the user.
  print("Enter the exam score: ")
  exam_score = input()

  # Check if the exam name is a continuous assessment test or an end-of-course exam.
  if exam_name in ["Continuous Assessment Test", "CAT"]:
    exam_type = "CAT"
  elif exam_name in ["End Course Exam", "ECE"]:
    exam_type = "ECE"
  else:
    print("Invalid exam name.")
    return

  # Insert the exam results into the database.
  cursor.execute('INSERT INTO exam_results (student_id, date_taken, exam_score, course, class_tutor, exam_type) VALUES (%s, %s, %s, %s, %s, %s)',
              (student_id, date_taken, exam_score, course_name, class_tutor, exam_type))

  # Commit the changes to the database.
  connection.commit()

  # Close the connection to the database.
  connection.close()

  print('Exam Results Posted')

