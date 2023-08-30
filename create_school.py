import logging
from contdb import connect_to_database

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', filename='log.log', datefmt='%Y-%m-%d %H:%M:%S')

# Get the database connection.
db = connect_to_database()

def create_school(first_name):
  """Creates a school and returns its name."""

  # Ask the user for the name of the school.
  school_name = input("Enter the name of the school: ")
  school_addr = input("Enter the address of the school: ")
  school_County = input("Enter County where school is located: ")
  school_phone = input("Enter the phone of the school: ")
  school_level = input("What level of education school offers: ") # Primary, sec, poly college, un
  school_type = input("Enter the gender arrangement of the school: ") # Mixed day, mixed boaders, monosex day, monosex boarders, college_style
  learners_type = input("Enter the type of leaners at school: ") # conventional, special

  # Log school creation info
  logging.info("Created school: {}".format(school_name))

  # Create a cursor object.
  cursor = db.cursor()

  # school_name = create_school(first_name)
  cursor.execute(f"INSERT INTO schools (school_name, school_County, school_level, school_type, learners_type, school_addr, school_phone) VALUES (%s, %s, %s, %s, %s, %s, %s)", (school_name, school_County, school_level, school_type, learners_type, school_addr, school_phone))
  db.commit()

    # Log database commit for school creation info
  logging.info(
      "Created school: {} by user {} commited to database".format(school_name, first_name))

  print("School created successfully.")


  # Return the school name.
  return school_name

def create_classes(first_name):
  """Creates a class and returns its name."""

  # Ask the user for the name of the school.
  class_name = input("Enter the name of the class: ")
  streams_number = int(input("How many streams does class have?: "))
  max_learners = input("Enter the maximum learners class accomodates: ")

  streams = 0
  stream_names = []
  while streams_number > streams:

    if streams_number == 1:
      stream_name = class_name
    else:
      stream_name = class_name + '_stream_' + str(streams + 1)
    
    streams +=1
    stream_names.append(stream_name)
  print(stream_names)

  # logging.info("Created class: {} and its streams".format(class_name))
  logging.info(
      "Created class: {} by user {} and its streams".format(class_name, first_name))


  # Return the school name.
  return class_name


