import psycopg2
import datetime
import os
import sys
import shutil

def connect_to_database():
  """Connects to the database."""
  # Read the .env file: Get variablesss .
  with open(".env") as f:
    env_vars = f.read().splitlines()

  DB_USERNAME = env_vars[0].split("=")[1]
  DB_PASSWORD = env_vars[1].split("=")[1]

  # Get the database connection string.
  # connection_string = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost/school"
  # connection_string = "postgresql://charles:Guide147@localhost/school"
  connection_string = "postgresql://charles:Guide147@postgres/school"
  # Connect to the database.
  connection = psycopg2.connect(connection_string)
  if not connection.closed:
    print("DB Connection is active.")
  else:
    print("Connection is not active.")

  return connection



# def insert_student_data(student_name, student_id):
#   """Inserts student data into the database."""

#   # Connect to the database.
#   connection = connect_to_database()

#   # Create a cursor object.
#   cursor = connection.cursor()

#   # Check if the student data already exists in the database.
#   query = "SELECT id FROM students WHERE name = '{}'".format(student_name)
#   cursor.execute(query)

#   student_id_exists = cursor.fetchone() is not None

#   if student_id_exists:
#     # The student data already exists in the database.
#     print('Student data already exists in the database.')
#     return

#   # Insert the student data into the database.
#   query = "INSERT INTO students (name, id) VALUES ('{}', {})".format(
#       student_name, student_id)
#   cursor.execute(query)

#   # Commit the changes to the database.
#   connection.commit()

#   # Close the cursor.
#   cursor.close()

#   # Close the connection to the database.
#   connection.close()


# def main():
#   # Insert some student data into the database.
#   try:
#     insert_student_data('John Doe', 1)
#     insert_student_data('Jane Doe', 2)
#   except psycopg2.Error as e:
#     print('Error inserting student data: {}'.format(e))

#   print('Inserted to Db')


# if __name__ == "__main__":
#   main()
# connect_to_database()