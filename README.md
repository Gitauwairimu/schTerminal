<!-- # schTerminal
To use this application:
Reliquisites;
1. Install postgres, Python3, Pip and Virtual env in a Linux System
2. Fork the repository - https://github.com/Gitauwairimu/schTerminal.git
3. Clone the Git repository using:
     git clone https://github.com/Gitauwairimu/schTerminal.git
4. Enter the cloned repository directory:
     cd schTerminal
5. Connect the repository with its remote to enable pulls and pushes
6. Set up a .gitignore and an .env files
7. Configure Postgres - Create database and a user, give permisions to te user
     psql -d postgres
     CREATE DATABASE school;
     CREATE USER charles WITH PASSWORD 'Guide147';
     GRANT ALL PRIVILEGES ON DATABASE school TO charles;
8. Obtain a Slack SLACK_WEBHOOK_URL for Slack notifications
9. Update .env with credentials for the postgres, Slack and Twilio
10. Run pip to install modules needed:
     pip install -r requirements.txt
11. Obtain a twilio token and update the .env file
12. Run the applcation
      python role_menu.py -->


# schTerminal

schTerminal is a school management system designed to streamline the day-to-day operations of educational institutions. It provides a user-friendly interface for managing students, teachers, classes, and schedules.

## Installation and Setup

### Prerequisites

* Install PostgreSQL, Python3, Pip, and Virtualenv on a Linux system.
* Create a GitHub account if you don't already have one.

### Steps

1. Fork the repository: https://github.com/Gitauwairimu/schTerminal.git
2. Clone the Git repository using:
```bash
git clone [https://github.com/Gitauwairimu/schTerminal.git](https://github.com/Gitauwairimu/schTerminal.git)



Enter the cloned repository directory:

Bash

cd schTerminal


Connect the repository with its remote to enable pulls and pushes:

Bash

git remote add origin https://github.com/Gitauwairimu/schTerminal.git

5. Create a `.gitignore` file to exclude unnecessary files from version control.
6. Create an `.env` file to store environment variables for database credentials and external services like Slack and Twilio.
7. Configure PostgreSQL:
   - Create the database `school`:
sql
psql -d postgres
CREATE DATABASE school;


    Create a user named dbuser with password dbuserpaswword:

SQL

CREATE USER charles WITH PASSWORD 'Guide147';



    Grant all privileges on the school database to the dbuser user:

SQL

GRANT ALL PRIVILEGES ON DATABASE school TO dbuser;


Configuration

    Obtain a Slack SLACK_WEBHOOK_URL for Slack notifications.
    Update the .env file with the credentials for PostgreSQL, Slack, and Twilio.
    Install the required Python modules:

Bash

pip install -r requirements.txt



    Obtain a Twilio token and update the .env file.

Running the Application

To start the application, run the following command from the project directory:
Bash

python role_menu.py


This will launch the main menu of the application, allowing you to manage various aspects of school operations.

