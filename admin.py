import psycopg2
from contdb import connect_to_database

# Create a database connection.
db = connect_to_database()

# Create a cursor object.
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
    # role = input("Enter Role: ")
#   print(roles.keys())
#   role = role.keys

  return role

def create_user(role):
  """Creates a new user with the given role."""
  # Get the name, email, password, and role from the user.
  role = get_role()
  cursor = db.cursor()
  print(role)


  # Get the user's name.
  first_name = input("Enter the user's name: ")
  surname = input("Enter the user's surname name: ")
  email = input("Enter the user's email address: ")
  password = input("Enter the user's password: ")

   # Determine the table to save the user to.
  if role == "2":
    table_name = "students"
  elif role == "3":
    table_name = "teachers"
  elif role == "1":
    table_name = "administrators"
  else:
    raise ValueError("Invalid role")

  # Create a SQL statement to insert the student into the database.
#   sql = """
#   INSERT INTO students (student_adm, first_name, surname, email, password, role)
#   VALUES (nextval('student_adm_seq'), %s, %s, %s, %s, %s)
#   """
  if role != "3":
  # Insert the user's data into the table.
    cursor.execute(f"INSERT INTO {table_name} (first_name, surname, email, password, role) VALUES (%s, %s, %s, %s, %s)",
                 (first_name, surname, email, password, role))
  else:
    identity_number = input("Enter the teacher's National Identity Number: ")
    identity_number = int(identity_number)
    department = input("Enter the teacher's department: ")
    cursor.execute(f"INSERT INTO {table_name} (first_name, surname, email, password, role, identity_number, department) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                 (first_name, surname, email, password, role, identity_number, department))
  # Execute the SQL statement.
#   cursor.execute(sql, (first_name, surname, email, password, role))

  # Commit the changes to the database.
  db.commit()
  print(f'User created as {role}')
  
def get_all_data():
  """Gets all data from the database and prints it in the terminal."""

  # Get a cursor object.
  cursor = db.cursor()

  # Get all data from the students table.
  sql = "SELECT * FROM teachers"
  cursor.execute(sql)

  # Print all data.
  for row in cursor:
    print(row)


# if __name__ == "__main__":
#   # Get the role of the user.
#   role = get_role()

#   # # Create a new user with the given role.
#   create_user(role)

#   # # Get all data from the database and print it in the terminal.
#   get_all_data()

def admin_menu():
  """Displays the admin menu and allows the user to select an option."""

  print("1. Create User")
  print("2. Edit User")
  print("3. Delete User")
  print("4. Back")

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
    return
  else:
    print("Invalid choice")
    admin_menu()

def delete_user():
  pass


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
  # sql = f"SELECT * FROM teachers WHERE identity_number = {identity_number}"
  
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

  sql = f"UPDATE administrators SET first_name = '{new_first_name}', surname = '{new_surname}', email = '{new_email}', password = '{new_password}' WHERE admin_no = {admin_no}"
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

  # Get the database connection.
  # db = connect_to_database()

  # Create a cursor object.
  # cursor = db.cursor()

  # Get the user's data from the database.
  # sql = f"SELECT * FROM user WHERE id = {user_id}"
  # cursor.execute(sql)
  # user_data = cursor.fetchone()

  # Update the user's data.
  # new_name = input("Enter the new name: ")
  # new_surname = input("Enter the new surname: ")
  # new_email = input("Enter the new email address: ")
  # new_password = input("Enter the new password: ")

  # sql = f"UPDATE users SET name = '{new_name}', surname = '{new_surname}', email = '{new_email}', password = '{new_password}' WHERE id = {user_id}"
  # cursor.execute(sql)

  # Commit the changes to the database.
  # db.commit()

  # Print a message to confirm that the user was edited.
  print("User edited")

def login_admin():
  # Check if the administrator exists.
  cursor.execute(f"SELECT COUNT(*) FROM administrators WHERE admin_no = 1;")
  count = cursor.fetchone()[0]


  if count == 0:
    # No administrator exists, so register one.
    print("No administrator exists. Registering a new administrator...")
    first_name = input("Enter the user's first name: ")
    surname = input("Enter the user's surname: ")
    email = input("Enter the user's email address: ")
    password = input("Enter the user's password: ")
    cursor.execute(f"INSERT INTO admin (first_name, surname, email, password, administrator) VALUES (%s, %s, %s, %s, %s)",
                 (first_name, surname, email, password, 1))
    conn.commit()
    print("Administrator registered successfully.")

  # The administrator already exists, so log in.
  login()


def login():
  # Get the admin's identity number.
  admin_no = input("Enter the administrator's identity number: ")

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

  if password == entered_password:
    # The password matches. The administrator is logged in.
    print("The administrator is logged in.")
    # Display the admins_menu.
    admin_menu()
  else:
    # The password does not match.
    print("The password does not match.")



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
  get_all_data()

if __name__ == "__main__":
#   # Call the main function.
  user()
# edit_user(user_id)