# Pip install all modules
# pip install-r modules.txt

# Create a postgres database called 'school'
# sudo -u postgres psql -c "CREATE DATABASE school;"

# Create a postgres database user called charles

# Alter postgres user (charles) password
# sudo -u postgres psql


# change your own db login details in database.cfg

#!/bin/bash

# Connect to the PostgreSQL database
# psql -h localhost -U postgres -d my_database

#!/bin/bash

# Get the user input for the charles user
read -p "Enter the user's database username: " user_name

# Create the school database as the charles user
if [ -z "$user_name" ]; then
  echo "Please enter a username"
  exit 1
fi

# Create the school database as the charles user
psql -h localhost -U Postgres -c "CREATE DATABASE daima;"

# Connect to the school database as the charles user
psql -h localhost -U $user_name -d school


# Grant the charles user create and select permissions on the school database
#sudo -u postgres psql -c "GRANT CREATE, SELECT ON DATABASE school TO charles;"







# Run the SQL statements
for sql_statement in $(cat sql_statements.txt); do
  echo "Running $sql_statement"
  psql -c "$sql_statement"
done