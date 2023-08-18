from contact_teacher import send_email
from library import library_menu
import datetime
import psycopg2

from contdb import connect_to_database

def connect_to_database():
  """Connects to the database."""

  # Get the database connection string.
  connection_string = "postgresql://charles:Guide147@localhost/school"

  # Connect to the database.
  connection = psycopg2.connect(connection_string)

  return connection


def get_student_id(student_name):
  """Gets the student ID for the student name."""

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor object.
  cursor = connection.cursor()

  # Select the student ID from the students table where the student name is equal
  # to the student name passed in.
  query = """
    SELECT id FROM students
    WHERE name = %s;
  """

  # Convert the student name to a Python string.
  student_name_string = str(student_name)

  # Execute the query.
  cursor.execute(query, (student_name_string,))

  record = cursor.fetchone()

  cursor.close()

  connection.close()

  # If there is no record, then the student ID is None.
  if not record:
    return None

  # Otherwise, the student ID is the value in the id column.
  return record[0]


def get_attendance_records(student_name):
  """Returns the attendance records for a student."""

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor object.
  cursor = connection.cursor()

  # Query the database for the student's attendance records.
  query = "SELECT date, is_present FROM attendance WHERE id IS NOT NULL"
  cursor.execute(query)

  # Create a dictionary of attendance records.
  attendance_records = {}
  for row in cursor:
    date = row[0]
    is_present = row[1]
    attendance_records[date] = is_present

  # Close the cursor.
  cursor.close()

  # Close the connection to the database.
  connection.close()

  return attendance_records

def attendance_menu():
  """Displays a menu of options for Attendance."""

  print("Welcome to the attendance menu.")
  print("What would you like to do?")
  print('                                            ')
  print('                                            ')


  print("1. Register your attendance.")
  print("2. View your attendance.")

  choice = input("Enter your choice: ")

  if choice == "1":
    # view_grades()
    create_attendance()
  elif choice == "2":
    # view_class_schedule()
    check_attendance()
  else:
    print("Invalid choice.")


def student_menu():
  """Displays a menu of options for students."""

  print("Welcome to the student menu.")
  print("What would you like to do?")
  print('                                            ')
  print('                                            ')


  print("1. View your grades.")
  print("2. View your class schedule.")
  print("3. Submit assignments.")
  print("4. Check your attendance.")
  print("5. Contact your teacher.")
  print("6. Access the school's library.")
  print("7. Sign up for extracurricular activities.")
  print("8. Quit.")

  print('                                            ')

  choice = input("Enter your choice: ")

  if choice == "1":
    # view_grades()
    send_email()
  elif choice == "2":
    # view_class_schedule()
    send_email()
  elif choice == "3":
    # submit_assignments()
    send_email()
  elif choice == "4":
    attendance_menu()
    # check_attendance()
  elif choice == "5":
    to_email = input("Enter the teachers's email address: ")
    subject = input("Enter the subject: ")
    body = input("Enter the body of the email: ")
    sender_email = input("Send from what email? ")
    password = input("Enter the password of the email: ")
    print('Sending Email: Wait for Confirmation')
    send_email(to_email, subject, body, sender_email, password)
    # contact_teacher()
  elif choice == "6":
    # access_library()
    library_menu()
  elif choice == "7":
    # sign_up_activities()
    send_email()
  elif choice == "8":
    print("Goodbye!")
    exit()
  else:
    print("Invalid choice.")

def save_attendance_record(attendance_record):
  """Saves the attendance record to the database."""

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor object.
  cursor = connection.cursor()

  # Get the student ID.
  student_id = get_student_id(attendance_record["student_name"])

  # If the student ID is None, then raise an error.
  if student_id is None:
    # raise ValueError("Student not found.")
    query = """
    INSERT INTO attendance (date, is_present, student_name)
    VALUES (%s, %s, %s);
  """

  # Convert the attendance record to a Python tuple.
  attendance_record_string = (
      attendance_record["date"],
      attendance_record["is_present"],
      attendance_record["student_name"]
  )

  # Execute the query.
  cursor.execute(query, attendance_record_string)

  connection.commit()

  cursor.close()

  connection.close()

  # Print a confirmation message.
  print("Attendance record saved.")


def create_attendance():
  """Creates an attendance record for the student."""

  # Get the student name.
  student_name = input("Enter your name: ")
#   student_id = input("Enter your student Id: ")

  # Get the date.
  date = input("Enter the date [YYYY-MM-DD] ")

  # Create the attendance record.
  attendance_record = {
      "student_name": student_name,
      "date": date,
      "is_present": True
  }

  # Save the attendance record to the database.
  save_attendance_record(attendance_record)

  # Print a confirmation message.
  print("Attendance record created.")

def check_attendance():
  """Checks the student's attendance for the current day."""

  # Get the student's name.
  student_name = input("Enter your name: ")

  # Get the current date.
  current_date = datetime.date.today()

  # Check the student's attendance for the current day.
  attendance_records = get_attendance_records(student_name)

  if current_date in attendance_records:
    is_present = attendance_records[current_date]
  else:
    is_present = False

  # Print the student's attendance status.
  if is_present:
    print("You are present today.")
  else:
    print("You are absent today.")


