import psycopg2
import datetime
import os
import sys
import shutil

def connect_to_database():
  """Connects to the database."""
  # Read the .env file: Get variablesss .
  # with open(".env") as f:
  #   env_vars = f.read().splitlines()

  # DB_USERNAME = env_vars[0].split("=")[1]
  # DB_PASSWORD = env_vars[1].split("=")[1]

  # Get the database connection string.
  # connection_string = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost/school"
 
  # Postgres RDS Connection
  # connection_string = (host='rds.amazonaws.com',
  #       port='5432',
  #       database='db',
  #       user='postgrescharles',
  #       password='qwertyqwerty')

  """Connects to the database using values from a Kubernetes secret."""
  
  # host = os.getenv("DB_HOST")
  # port = os.getenv("DB_PORT")
  # database = os.getenv("DB_DATABASE")
  # user = os.getenv("DB_USER")
  # password = os.getenv("DB_PASSWORD")




  connection_string = {
    "host": "os.getenv('DB_HOST')",
    "port": "os.getenv('DB_PORT')",
    "database": "os.getenv('DB_DATABASE')",
    "user": "os.getenv('DB_USER')",
    "password": "os.getenv('DB_PASSWORD')"
  }
 
  # Construct the connection string as a string
  connection_string = f"host={connection_string['host']} port={connection_string['port']} dbname={connection_string['database']} user={connection_string['user']} password={connection_string['password']}"


  # Connect to the database.
  connection = psycopg2.connect(connection_string)
  
  if not connection.closed:
    print("DB Connection is active.")
  else:
    print("Connection is not active.")

  return connection


