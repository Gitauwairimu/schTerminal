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
git clone https://github.com/Gitauwairimu/schTerminal.git



3. Enter the cloned repository directory:

Bash

cd schTerminal


4. Connect the repository with its remote to enable pulls and pushes:

Bash

git remote add origin https://github.com/Gitauwairimu/schTerminal.git

5. Create a `.gitignore` file to exclude unnecessary files from version control.
6. Create an `.env` file to store environment variables for database credentials and external services like Slack and Twilio.
7. Configure PostgreSQL:
   - Create the database `school`:

psql -d postgres
CREATE DATABASE school;


8 .Create a user named dbuser with password dbuserpaswword:


CREATE USER charles WITH PASSWORD 'dbuserpaswword';


9. Grant all privileges on the school database to the dbuser user:


GRANT ALL PRIVILEGES ON DATABASE school TO dbuser;


10. Configuration

   1. Obtain a Slack SLACK_WEBHOOK_URL for Slack notifications.
   2. Update the .env file with the credentials for PostgreSQL, Slack, and Twilio.
   3. Install the required Python modules:

Bash

pip install -r requirements.txt


Obtain a Twilio token and update the .env file.

11. Running the Application

To start the application, run the following command from the project directory:
Bash

python role_menu.py


This will launch the main menu of the application, allowing you to manage various aspects of school operations.

