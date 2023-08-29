def create_school():
  """Creates a school and returns its name."""

  # Ask the user for the name of the school.
  school_name = input("Enter the name of the school: ")
  school_addr = input("Enter the address of the school: ")
  school_County = input("Enter County where school is located: ")
  school_phone = input("Enter the phone of the school: ")
  school_level = input("What level of education school offers: ") # Primary, sec, poly college, un
  school_type = input("Enter the gender arrangement of the school: ") # Mixed day, mixed boaders, monosex day, monosex boarders, college_style
  learners_type = input("Enter the type of leaners at school: ") # conventional, special

  print(f'School Name: {school_name}')
  print(f'County: {school_County}')
  print(f'School Level: {school_level}')
  print(f'Type of School: {school_type}')
  print(f'Type of Learners: {learners_type}')
  print(f'School Address: {school_addr}')
  print(f'School Phone: {school_phone}')


  # Return the school name.
  return school_name

def create_classes():
  """Creates a class and returns its name."""

  # Ask the user for the name of the school.
  class_name = input("Enter the name of the class: ")
  streams_number = int(input("How many streams does class have?: "))
  max_learners = input("Enter the maximum learners class accomodates: ")

  streams = 0
  stream_names = []
  while streams_number > streams:
    stream_name = class_name + '_stream_' + str(streams + 1)
    streams +=1
    stream_names.append(stream_name)
  print(stream_names)

  # Return the school name.
  return class_name


if __name__ == "__main__":
  # # Create the school.
  # school_name = create_school()

  # # Print the name of the school.
  # print(f"School Name: {school_name}.")
  create_classes()
