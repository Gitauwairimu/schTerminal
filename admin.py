import requests, os, sys, shutil
import psycopg2
from contdb import connect_to_database
from sms import send_sms
import hashlib
# from notifications import send_slack_message
from notifications import send_slack_message

# Read the .env file: Get variablesss .
with open(".env") as f:
  env_vars = f.read().splitlines()

SLACK_WEBHOOK_URL = env_vars[2].split("=")[1]

# # Create a database connection.
db = connect_to_database()

# # Create a cursor object.
cursor = db.cursor()

def get_role():
  """Displays a menu of roles for user registration."""

  print("Welcome to the roles menu.")
  print("Choose Role of user to be registered?")
  print('                                            ')
  print('                                            ')


  print("1. Administrator.")
  print("2. Student")
  print("3. Teaching Staff.")
  print("4. Support Staff.")
  print("5. Quit.")

  print('                                            ')

  role = input("Enter Role: ")
  roles = {
    "1": "administrator",
    "2": "student",
    "3": "teaching staff",
    "4": "support staff"
  }


  while role not in roles.keys():
    print("Invalid role. Please choose a valid role.")
    get_role()

  role = {roles[role]}
  role = ','.join(role)

  return role

# def get_role():
#   """Displays a menu of roles for user registration."""

#   print("Welcome to the roles menu.")
#   print("Choose Role of user to be registered?")
#   print('                                            ')
#   print('                                            ')


#   print("1. Administrator.")
#   print("2. Student")
#   print("3. Teaching Staff.")
#   print("4. Support Staff.")
#   print("5. Quit.")

#   print('                                            ')

#   role = input("Enter Role: ")
#   roles = {
#     "1": "administrator",
#     "2": "student",
#     "3": "teaching staff",
#     "4": "support staff"
#   }


#   while role not in roles.keys():
#     print("Invalid role. Please choose a valid role.")
#     # role = input("Enter Role: ")
# #   print(roles.keys())
# #   role = role.keys

#   return role



def create_user(role):
  """Creates a new user with the given role."""
  print(role)


  # Get the user's details.
  first_name = input(f"Enter the {role}'s first name: ")
  surname = input(f"Enter the {role}'s surname name: ")
  email = input(f"Enter the {role}'s email address: ")
  password = input(f"Enter the {role}'s password: ")

  # Hash the password.
  password = hashlib.sha256(password.encode()).hexdigest()


   # Determine the table to save the user to.
  if role == "student":
    table_name = "students"
  elif role == "teaching staff":
    table_name = "teachers"
  elif role == "administrator":
    table_name = "administrators"
  else:
    raise ValueError("Invalid role")

  admin_no = None
  if role == "administrator":
    # Insert the user's data into the table.
    admin_mobile = input("Enter the admin's mobile phone number: ")

    cursor.execute(f"INSERT INTO {table_name} (first_name, surname, email, admin_mobile, password, role) VALUES (%s, %s, %s, %s, %s, %s)",
                 (first_name, surname, email, admin_mobile, password, role))

  elif role == "student":
  # Insert the user's data into the table.
    cursor.execute(f"INSERT INTO {table_name} (first_name, surname, email, password, role) VALUES (%s, %s, %s, %s, %s)",
                 (first_name, surname, email, password, role))
    
   
  elif role == "teaching staff":
    # role = 'teacher'
    identity_number = input("Enter the teacher's National Identity Number: ")
    identity_number = int(identity_number)
    department = input("Enter the teacher's department: ")
    cursor.execute(f"INSERT INTO {table_name} (first_name, surname, email, password, role, identity_number, department) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                 (first_name, surname, email, password, role, identity_number, department))

  # Commit the changes to the database.
  db.commit()
  # db.close()

  # cursor = db.cursor()
  # Get the last admin number from the database.
  # Execute the query.
  cursor.execute("""
  SELECT admin_no, admin_mobile, first_name FROM administrators ORDER BY admin_no DESC LIMIT 1;
  """)

  # Fetch the results of the query.
  results = cursor.fetchone()

  # Use the values from the results.
  admin_no = results[0]
  admin_mobile = results[1]
  first_name = results[2]


  send_slack_message(admin_no, first_name, admin_mobile)

  if role == "1":
    send_sms(to=admin_mobile, body=f"Welcome {first_name}, Use admin number: {admin_no} to login. Account created.")


def get_all_data():
  """Gets all data from the database and prints it in the terminal."""

  # Get all data from the students table.
  sql = "SELECT * FROM teachers"
  cursor.execute(sql)

  # Print all data.
  for row in cursor:
    print(row)


def admin_menu():
  """Displays the admin menu and allows the user to select an option."""

  print("1. Create User")
  print("2. Edit User")
  print("3. Delete User")
  print("4. View Users")
  print("5. Register Lecture Halls")
  print("6. Back")

  print('............................................')
  print('                                            ')
  print('                                            ')

  choice = input("Enter your choice: ")

  if choice == "1":
    user()
  elif choice == "2":
    edit_user()
  elif choice == "3":
    delete_user()
  elif choice == "4":
    view_all_users()
  elif choice == "5":
    register_lecture_hall()
  elif choice == "6":
    admin_menu()
  else:
    print("Invalid choice")
    admin_menu()


def register_lecture_hall():
  """Registers a new lecture hall in the database."""

  # Prompt the user for the lecture hall name.
  lecture_hall_name = input("Enter the lecture hall name: ")
  
  # Prompt the user for the lecture hall capacity.
  capacity = input("Enter the lecture hall capacity: ")

  # Prompt for hall location
  location = input("Enter the location of hall: ")

  # Create a SQL statement to insert the lecture hall into the database.
  sql = f"""
    INSERT INTO lecture_halls (lecture_hall_name, capacity, location)
    VALUES ('{lecture_hall_name}', {capacity}, '{location}')
  """
  cursor.execute(sql)

  # Commit the changes to the database.
  db.commit()

  print('                                               ')

  print(f'Registered Lecture Hall: {lecture_hall_name}')

  print('                                               ')

def edit_student():
  """Edits an existing student in the database."""

  # Get the database connection.
  # db = connect_to_database()

  # # Create a cursor object.
  # cursor = db.cursor()
  student_adm = input("Enter student admission number: ")
  # Get the student's data from the database.
  sql = f"SELECT * FROM students WHERE student_adm = {student_adm}"
  cursor.execute(sql)
  admin_data = cursor.fetchone()

  # Update the student's data.
  new_first_name = input("Enter the new name: ")
  new_surname = input("Enter the new surname: ")
  new_email = input("Enter the new email address: ")
  new_password = input("Enter the new password: ")

  # Hash the new_password
  new_password = hashlib.sha256(new_password.encode()).hexdigest()

  sql = f"UPDATE students SET first_name = '{new_first_name}', surname = '{new_surname}', email = '{new_email}', password = '{new_password}' WHERE student_adm = {student_adm}"
  cursor.execute(sql)

  # Commit the changes to the database.
  db.commit()

  # Print a message to confirm that the student was edited.
  print("Student edited")


def edit_teacher():
  """Edits an existing teacher in the database."""

  # Get the database connection.
  # db = connect_to_database()

  # # Create a cursor object.
  # cursor = db.cursor()
  identity_number = input("Enter teacher's national identity number to edit: ")
  # Get the teacher's data from the database.
  sql = f"SELECT * FROM teachers WHERE CAST(identity_number AS integer) = {identity_number}"
  
  if sql:
    cursor.execute(sql)
  else:
    print("SQL statement is empty")

  admin_data = cursor.fetchone()

  # Update the teacher's data.
  new_first_name = input("Enter the new name: ")
  new_surname = input("Enter the new surname: ")
  new_email = input("Enter the new email address: ")
  new_password = input("Enter the new password: ")

  # Hash the new_password
  new_password = hashlib.sha256(new_password.encode()).hexdigest()


  sql = f"UPDATE teachers SET first_name = '{new_first_name}', surname = '{new_surname}', email = '{new_email}', password = '{new_password}' WHERE CAST(identity_number AS integer) = {identity_number}"
  cursor.execute(sql)

  # Commit the changes to the database.
  db.commit()

  # Print a message to confirm that the teacher was edited.
  print("Teacher details updated")


def edit_admin():
  """Edits an existing administrator in the database."""

  # Get the database connection.
  # db = connect_to_database()

  # # Create a cursor object.
  # cursor = db.cursor()
  admin_no = input("Enter admin number of admin to edit: ")
  # Get the administrator's data from the database.
  sql = f"SELECT * FROM administrators WHERE admin_no = {admin_no}"
  cursor.execute(sql)
  admin_data = cursor.fetchone()

  # Update the administrator's data.
  new_first_name = input("Enter the new name: ")
  new_surname = input("Enter the new surname: ")
  new_email = input("Enter the new email address: ")
  new_password = input("Enter the new password: ")
  new_admin_mobile = input("Enter the new mobile phone number: ")

  # Hash the new_password
  new_password = hashlib.sha256(new_password.encode()).hexdigest()


  sql = f"UPDATE administrators SET first_name = '{new_first_name}', surname = '{new_surname}', email = '{new_email}', password = '{new_password}', admin_mobile = '{new_admin_mobile}' WHERE admin_no = {admin_no}"
  cursor.execute(sql)

  # Commit the changes to the database.
  db.commit()

  # Print a message to confirm that the administrator was edited.
  print("Administrator edited")


def edit_user():
  """Edits an existing user in the database."""

  print('Choose Category of User to Edit')
  # user_id = input("Enter ID of user to edit: ")

  print('                                            ')
  print('                                            ')

  print("1. Administrator")
  print("2. Teacher")
  print("3. Support Staff")
  print("4. Student")

  print('............................................')
  print('                                            ')
  print('                                            ')

  user_to_edit = input("Enter your choice (1-4): ")

  try:
    user_to_edit = int(user_to_edit)
  except ValueError:
    print("Invalid user category. Please enter a number between 1 and 4.")
    return None

  if user_to_edit == 1:
    edit_admin()
  elif user_to_edit == 2:
    edit_teacher()
  elif user_to_edit == 3:
    edit_support_staff()
  elif user_to_edit == 4:
    edit_student()
  else:
    print('You must choose from existing categories')

 
  print("User edited")

def login_admin():
  # Check if the administrator exists.
  cursor.execute(f"SELECT COUNT(*) FROM administrators WHERE admin_no >= 1;")
  count = cursor.fetchone()[0]


  if count == 0:
    # No administrator exists, so register one.
    print('                                                      ')
    print("No administrator exists. Registering as the administrator...")
    print('                                                      ')
    first_name = input("Enter the admin's first name: ")
    surname = input("Enter the admin's surname: ")
    email = input("Enter the admin's email address: ")
    password = input("Enter the admin's password: ")
    admin_mobile = input("Enter the admin's mobile phone number: ")
    role = 'administrator'

    # Hash the password that the user entered.
    password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute(f"INSERT INTO administrators (first_name, surname, email, password, role, admin_mobile) VALUES (%s, %s, %s, %s, %s, %s)",
                 (first_name, surname, email, password, role, admin_mobile))
    db.commit()

    # Check if the school exists.
    cursor.execute(f"SELECT COUNT(*) FROM schools;")
    count = cursor.fetchone()[0]

    if count == 0:
      # No school exists, so create one.
      school_name = input("Enter the school's name: ")
      cursor.execute(f"INSERT INTO schools (name) VALUES (%s)", (school_name,))
      db.commit()
      print("School created successfully.")

    print("Administrator registered successfully.")
    print(".........................................")
    print('Login Now')
    print(".........................................")

  # The administrator already exists, so log in.
  login()


def login():
  # Get the admin's identity number.
  admin_no = input("Login: Enter admin number: ")

  # Check if the administrator exists.
  cursor.execute(f"SELECT * FROM administrators WHERE admin_no = {admin_no};")
  row = cursor.fetchone()

  if row is None:
    # The administrator does not exist.
    print("The administrator does not exist.")
    return

  # Get the administrator's password.
  password = row[4]

  # Check if the password matches.
  entered_password = input("Enter the administrator's password: ")

    # Hash the new_password
  entered_password = hashlib.sha256(entered_password.encode()).hexdigest()


  if password == entered_password:
    # The password matches. The administrator is logged in.
    print("The administrator is logged in.")
    print('                                  ')
    # Display the admins_menu.
    admin_menu()
  else:
    # The password does not match.
    print("The password does not match.")

def delete_user():
  """Edits an existing user in the database."""

  print('Choose Category of User to delete')
  # user_id = input("Enter ID of user to edit: ")

  print('                                            ')
  print('                                            ')

  print("1. Delete Administrator")
  print("2. Delete Teacher")
  print("3. Delete Support Staff")
  print("4. Delete Student")

  print('............................................')
  print('                                            ')
  print('                                            ')

  user_to_delete = input("Enter your choice (1-4): ")

  try:
    user_to_delete = int(user_to_delete)
  except ValueError:
    print("Invalid user category. Please enter a number between 1 and 4.")
    return None

  if user_to_delete == 1:
    delete_admin()
  elif user_to_delete == 2:
    delete_teacher()
  elif user_to_delete == 3:
    delete_support_staff()
  elif user_to_delete == 4:
    delete_student()
  else:
    print('You must choose from existing categories')

def delete_admin():
  admin_no = input('Enter admin_no of Admin to be deleted: ')
  # Check if the admin exists.
  cursor.execute(f"SELECT * FROM administrators WHERE admin_no = {admin_no};")
  row = cursor.fetchone()

  if row is None:
    # The admin does not exist.
    print("The admin does not exist.")
    return

  # Delete the admin.
  cursor.execute(f"DELETE FROM administrators WHERE admin_no = {admin_no};")
  db.commit()

  print("The admin has been deleted.")


def view_all_users():
  # Get all administrators.
  cursor.execute(f"SELECT * FROM administrators;")
  administrators = cursor.fetchall()

  # Get all teachers.
  cursor.execute(f"SELECT * FROM teachers;")
  teachers = cursor.fetchall()

  # Get all support staff.
  # cursor.execute(f"SELECT * FROM support_staff;")
  # support_staff = cursor.fetchall()

  # Get all students.
  cursor.execute(f"SELECT * FROM students;")
  students = cursor.fetchall()

  print ('                                         ')

  # Print all users.
  print("Administrators:")
  for administrator in administrators:
    print(administrator)

  print ('                                         ')

  print("Teachers:")
  for teacher in teachers:
    print(teacher)
  
  print ('                                         ')

  # print("Support staff:")
  # for support_staff in support_staff:
  #   print(support_staff)

  print("Students:")
  for student in students:
    print(student)
  
  print ('                                         ')



# if __name__ == "__main__":
  # Get the user ID of the user to edit.
  # user_id = input("Enter the user ID: ")
  # user_id = input("Enter ID of user to edit: ")

  # Edit the user.
  # edit_user(user_id)



def user():
  # Get the role of the user.
  role = get_role()

  # Create a new user with the given role.
  create_user(role)

  # Get all data from the database and print it in the terminal.
  # get_all_data()

# if __name__ == "__main__":
# #   # Call the main function.
#   user()
# # edit_user(user_id)