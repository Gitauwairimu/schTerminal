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
  school_name = create_school()

  # # Print the name of the school.
  # print(f"School Name: {school_name}.")
  create_classes()
