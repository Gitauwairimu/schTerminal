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
  connection_string = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost/school"
  # connection_string = "postgresql://charles:Guide147@localhost/school"
  # connection_string = "postgresql://charles:Guide147@postgres/school"
  # Connect to the database.
  connection = psycopg2.connect(connection_string)
  if not connection.closed:
    print("DB Connection is active.")
  else:
    print("Connection is not active.")

  return connection


