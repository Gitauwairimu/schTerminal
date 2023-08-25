from contdb import connect_to_database
import datetime

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

  return students



def take_daily_attendance():
  """Allows the teacher to take the daily attendance."""

  # Get a list of all the students in the class.
  students = view_all_students()

  # Create a dictionary to store the attendance of each student.
  attendance = {}

  # Get the list of courses from the database.
  connection = connect_to_database()

  cursor = connection.cursor()

  cursor.execute('SELECT class_name FROM class_schedule')
  courses = cursor.fetchall()

  # The name of the class for which attendance is being taken.
  # Choose a course from the list.
  print("Choose a course:")
  for index, course in enumerate(courses):
    print(f"{index + 1}. {course[0]}")
  choice = int(input("Choose Course: "))

  # Validate the input.
  if choice not in range(1, len(courses) + 1):
    raise ValueError("Invalid choice")

  class_name = courses[choice - 1][0] 

  # The date for which attendance is being taken
  try:
    print("Date attendance taken for (YYYY-MM-DD): ")
    date_attendance_for = input()

    # Convert the due date to a valid format.
    date_attendance_for = datetime.datetime.strptime(date_attendance_for, '%Y-%m-%d').strftime('%Y-%m-%d')


  except ValueError:
    print("Invalid date format. Please enter the date in the format YYYY-MM-DD")

  # The date the attendance was taken.
  date_attendance_taken = datetime.datetime.now()

  # Iterate over the students.
  for student in students:
    # Prompt the teacher to enter the student's attendance.
    attendance[student] = input(f"Enter {student}'s attendance (Present/Absent): ")

  # Save the attendance to the database.
  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor to execute SQL statements.
  cursor = connection.cursor()

  # # Insert the data into the table.
  # for student, attendance_status in attendance.items():
  #   cursor.execute('INSERT INTO attendance (student_id, attendance, date_attendance_for, class_name, date_attendance_taken) VALUES (%s, %s, %s, %s, %s)',
  #                 (student, attendance_status, date_attendance_for, class_name, date_attendance_taken))
  student_id = None

  for student, attendance_status in attendance.items():
    student_id = student[0]
    cursor.execute('INSERT INTO attendance (student_id, attendance, date_attendance_for, class_name, date_attendance_taken) VALUES (%s, %s, %s, %s, %s)',
                    (student_id, attendance_status, date_attendance_for, class_name, date_attendance_taken))


  # Commit the changes to the database.
  connection.commit()

  # Close the connection to the database.
  connection.close()

  print('Attendance Taken')

def view_attendance():
  """Allows the teacher to view the attendance for a particular date."""

  # Get the date for which the attendance is being viewed.
  print("Enter the date for which you want to view the attendance (YYYY-MM-DD): ")
    # The date for which attendance is being taken
  try:
    print("Date attendance taken for (YYYY-MM-DD): ")
    date_attendance_for = input()

    # Convert the due date to a valid format.
    date_attendance_for = datetime.datetime.strptime(date_attendance_for, '%Y-%m-%d').strftime('%Y-%m-%d')

  except ValueError:
    print("Invalid date format. Please enter the date in the format YYYY-MM-DD")


  # Get the list of students in the class.
  students = view_all_students()

  # Get the attendance for the specified date.
  connection = connect_to_database()

  cursor = connection.cursor()
  
  # declare a variable
  class_name = None

  date_attendance_for_str = str(date_attendance_for)

  # cursor.execute('SELECT student_id, class_name, attendance, date_attendance_taken FROM attendance WHERE date_attendance_for = %s',
  #                 (date_attendance_for_str,))

  cursor.execute('SELECT student_id, class_name, attendance, date_attendance_taken FROM attendance WHERE date_attendance_for = %s AND class_name = %s',
                  (date_attendance_for_str, class_name))

  # cursor.execute('SELECT student_id, class_name, attendance, date_attendance_taken FROM attendance WHERE date_attendance_for = %s',
  #                 (date_attendance_for))

  # cursor.execute('SELECT student_id, class_name, attendance, date_attendance_taken FROM attendance WHERE date_attendance_for = %s AND class_name = %s',
  #                 (date_attendance_for, class_name))
  attendance = cursor.fetchall()

  # Close the connection to the database.
  connection.close()

  # Print the attendance for the specified date.
  print("Student ID | Class Name | Attendance | Date Attendance Taken")
  for student_id, class_name, attendance_status, date_attendance_taken in attendance:
    print(f"{student_id:<10} | {class_name:<10} | {attendance_status:<10} | {date_attendance_taken}")

def update_attendance():
  """Allows the teacher to update the attendance for a particular student."""

  # Get the student ID.
  print("Enter the student ID: ")
  student_id = input()

  # Get the attendance status.
  print("Enter the attendance status (Present/Absent): ")
  attendance_status = input()

  # Get the date for which the attendance is being updated.
  print("Date attendance updated for (YYYY-MM-DD): ")
  date_attendance_for = input()

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor to execute SQL statements.
  cursor = connection.cursor()

  # Update the attendance.
  cursor.execute('UPDATE attendance SET attendance = %s WHERE student_id = %s AND date_attendance_for = %s',
                  (attendance_status, student_id, date_attendance_for))

  # Commit the changes to the database.
  connection.commit()

  # Close the connection to the database.
  connection.close()

  print(f"Attendance for student {student_id} updated")

