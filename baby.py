import requests, os, sys, shutil
import psycopg2
from contdb import connect_to_database
from sms import send_sms


# Read the .env file: Get variablesss .
with open(".env") as f:
  env_vars = f.read().splitlines()

SLACK_WEBHOOK_URL = env_vars[2].split("=")[1]

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


#   print(f'role.keys: {roles.keys}')
#   print(f'roles: {roles[role]}')

  while role not in roles.keys():
    print("Invalid role. Please choose a valid role.")
    get_role()
    # role = input("Enter Role: ")
#   print(roles.keys())
#   role = role.keys
  role = {roles[role]}
  role = ','.join(role)
  print(role)

  return roles

