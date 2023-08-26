import student, admin, teacher


def role_menu():
  """Displays a menu of roles and asks the user to choose one."""

  # Print the menu of roles.
  print("Please choose your role:")
  print("1. Administrator")
  print("2. Teacher")
  print("3. Guest")
  print("4. Student")

  # Create space
  print('............................................')
  print('                                            ')
  print('                                            ')
  
  # Get the user's choice.
  choice = input("Enter your choice (1-4): ")

  print('                                            ')

  # Validate the user's choice.
  try:
    choice = int(choice)
  except ValueError:
    print("Invalid choice. Please enter a number between 1 and 4.")
    return None

  if choice not in (1, 2, 3, 4):
    print("Invalid choice. Please enter a number between 1 and 4.")
    return None

  # Get the message to print.
  messages = {
    1: "You are an administrator.",
    2: "You are a teacher.",
    3: "You are a guest.",
    4: "You are a student.",
  }

  # Get the message.
  message = messages.get(choice)

  # Print the message.
  if message:
    print(message)
    print('............................................')
    print('                                            ')
    print('                                            ')


  # If the user is a student, call the student_menu() function.
  if choice == 4:
    student.student_menu()
  elif choice == 1:
    admin.login_admin()
  elif choice == 2:
    teacher.teacher_menu()




# This is the main function.
def main():
  # Get the user's role.
  role = role_menu()


if __name__ == "__main__":
  main()
