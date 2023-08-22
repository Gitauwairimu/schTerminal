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
    department = input("Enter the teacher's department: ")
    cursor.execute(f"INSERT INTO {table_name} (first_name, surname, email, password, role, identity_number, department) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                 (first_name, surname, email, password, role, identity_number, department))
  # Execute the SQL statement.
#   cursor.execute(sql, (first_name, surname, email, password, role))

  # Commit the changes to the database.
  db.commit()
  print('User created')

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


if __name__ == "__main__":
  # Get the role of the user.
  role = get_role()

  # Create a new user with the given role.
  create_user(role)

  # Get all data from the database and print it in the terminal.
  get_all_data()
