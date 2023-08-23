def teacher_menu():
  """Displays the teachers menu and allows the user to select an option."""

  print("1. Attendance")
  print("2. Post Exam Results")
  print("3. Post Class Schedule")
  print("4. View Students")
  print("5. Issue Homework")
  print("6. Back")

  print('............................................')
  print('                                            ')
  print('                                            ')

  choice = input("Enter your choice: ")

  if choice == "1":
    attendance_menu() 
  elif choice == "2":
    post_exam_results()
  elif choice == "3":
    post_classes()
  elif choice == "4":
    view_all_students()
  elif choice == "5":
    issue_homework()
  elif choice == "5":
    teacher_menu()
  else:
    print("Invalid choice")
    teacher_menu()

 # view and create functions

def attendance_menu():
  """Displays the attendance menu and allows the teacher to select an option."""

  print("1. Take Daily Attendance")
  print("2. View Attendance")
  print("3. Update Attendance")
  print("4. Back")

  print('............................................')
  print('                                            ')
  print('                                            ')

  choice = input("Enter your choice: ")

  if choice == "1":
    take_daily_attendance()
  elif choice == "2":
    view_attendance()
  elif choice == "3":
    update_attendance()
  elif choice == "4":
    attendance_menu()
  else:
    print("Invalid choice")
    attendance_menu()
