def create_school():
  """Creates a school and returns its name."""

  # Ask the user for the name of the school.
  school_name = input("Enter the name of the school: ")

  # Return the school name.
  return school_name


if __name__ == "__main__":
  # Create the school.
  school_name = create_school()

  # Print the name of the school.
  print(f"School Name: {school_name}.")
