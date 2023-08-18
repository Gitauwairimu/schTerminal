from contdb import connect_to_database

def get_library_records(student_name):
  """Gets the student's library records from the database."""

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor object.
  cursor = connection.cursor()

  # Query the database for the student's library records.
  query = "SELECT book_name FROM library_records WHERE student_name = '{}'".format(
      student_name)
  cursor.execute(query)

  # Create a list of books.
  library_records = []
  for row in cursor:
    book_name = row[0]
    library_records.append(book_name)

  # Close the cursor.
  cursor.close()

  # Close the connection to the database.
  connection.close()

  return library_records


def check_library_records():
  """Checks the student's library records."""

  # Get the student's name.
  student_name = input("Enter your name: ")

  # Get the student's library records from the database.
  library_records = get_library_records(student_name)

  # Print the student's library records.
  if library_records:
    for book in library_records:
      print(book)
  else:
    print("No library records found for student.")



def is_book_available(book_name):
  """Checks if the book is available."""

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor object.
  cursor = connection.cursor()

  # Query the database for the number of copies of the book.
  query = "SELECT COUNT(*) FROM books WHERE book_name = '{}'".format(book_name)
  cursor.execute(query)

  # Get the number of copies of the book.
  number_of_copies = cursor.fetchone()[0]

  # Close the cursor.
  cursor.close()

  # Close the connection to the database.
  connection.close()

  # The book is available if there are at least one copy of the book.
  return number_of_copies > 0

def get_number_of_books_borrowed(student_name):
  """Gets the number of books that a student has borrowed."""

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor object.
  cursor = connection.cursor()

  # Query the database for the number of books borrowed by the student.
  query = "SELECT COUNT(*) FROM library_records WHERE student_name = '{}'".format(
      student_name)
  cursor.execute(query)

  # Get the number of books borrowed.
  number_of_books_borrowed = cursor.fetchone()[0]

  # Close the cursor.
  cursor.close()

  # Close the connection to the database.
  connection.close()

  return number_of_books_borrowed


def is_student_allowed_to_borrow_book(student_name, book_name):
  """Checks if the student is allowed to borrow the book."""

  # Check if the book is available.
  is_available = is_book_available(book_name)
  if not is_available:
    return False

  # Check if the student has borrowed the maximum number of books.
#   max_books_allowed = get_max_books_allowed(student_name)
  max_books_allowed = 5
  number_of_books_borrowed = get_number_of_books_borrowed(student_name)
  if number_of_books_borrowed >= max_books_allowed:
    return False

  # The student is allowed to borrow the book.
  return True


def add_book_to_library_records(student_name, book_name):
  """Adds a book to the student's library records in the database."""

  # Get the book name from the user.

  # Check if the book is already in the student's library records.
  library_records = get_library_records(student_name)
  if book_name in library_records:
    print("The book is already in the student's library records.")
    return

  # Check if the student is allowed to borrow the book.
#   if not is_student_allowed_to_borrow_book(student_name, book_name):
#     print("The student is not allowed to borrow the book.")
#     return

  # Add the book to the student's library records in the database.
  add_book_to_library_records_db(student_name, book_name)

  print("Book added to library records.")



def add_book_to_library_records_db(student_name, book_name):
  """Adds a book to the student's library records in the database."""

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor object.
  cursor = connection.cursor()

  # Insert the book into the library records table.
  query = "INSERT INTO library_records (student_name, book_name, date_borrowed) VALUES ('{}', '{}', CURRENT_DATE)".format(
      student_name, book_name)
  cursor.execute(query)

  # Commit the changes to the database.
  connection.commit()

  # Close the cursor.
  cursor.close()

  # Close the connection to the database.
  connection.close()


def remove_book_from_library_records(student_name, book_name):
  """Removes a book from the student's library records."""

  # Check if the book is in the student's library records.
  library_records = get_library_records(student_name)
  if book_name not in library_records:
    print("The book is not in the student's library records.")
    return

  # Remove the book from the student's library records in the database.
  remove_book_from_library_records_db(student_name, book_name)

  print("Book removed from library records.")

def remove_book_from_library_records_db(student_name, book_name):
  """Removes a book from the student's library records in the database."""

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor object.
  cursor = connection.cursor()

  # Execute the query to delete the book from the library records table.
  query = "DELETE FROM library_records WHERE student_name = '{}' AND book_name = '{}'".format(
      student_name, book_name)
  cursor.execute(query)

  # Commit the changes to the database.
  connection.commit()

  # Close the cursor.
  cursor.close()

  # Close the connection to the database.
  connection.close()



def get_books_borrowed_today_by_student(student_name):
  """Gets the books borrowed today by the student."""

  # Connect to the database.
  connection = connect_to_database()

  # Create a cursor object.
  cursor = connection.cursor()


  # Select all the books from the library records table where the date borrowed is equal to
  # the current date and the student name is equal to the student name passed in.
  query = """
    SELECT book_name FROM library_records
    WHERE date_borrowed = CURRENT_DATE
    AND student_name = %s
  """

  # Convert the student name to a Python string.
  student_name_string = str(student_name)

  # Execute the query.
  cursor.execute(query, (student_name_string,))

  # Get the books borrowed today by the student.
  books_borrowed_today_by_student = []
  for row in cursor:
    book_name = row[0]
    books_borrowed_today_by_student.append(book_name)

  # Close the cursor.
  cursor.close()

  # Close the connection to the database.
  connection.close()

  return books_borrowed_today_by_student


def view_overdue_books():
  """Views the student's overdue books."""

  # Get the student's name.
  student_name = input("Enter your name: ")

  # Get the student's overdue books from the database.
#   overdue_books = get_overdue_books(student_name)
  overdue_books = get_books_borrowed_today_by_student(student_name)

  # Print the student's overdue books.
  if overdue_books:
    for book in overdue_books:
      print(book)
  else:
    print("No overdue books found.")


def library_menu():
  """Presents the library menu."""

  print("Welcome to the library menu.")
  print("What would you like to do?")
  print("1. Check library records")
  print("2. Add a book to library records")
  print("3. Remove a book from library records")
  print("4. View overdue books")
  print("5. Return to main menu")

  choice = input("Enter your choice: ")

  if choice == "1":
    check_library_records()
  elif choice == "2":
    student_name = input("Enter your name: ")
    book_name = input("Enter the name of the book: ")
    add_book_to_library_records(student_name, book_name)
  elif choice == "3":
    student_name = input("Enter your name: ")
    book_name = input("Enter the name of the book: ")
    remove_book_from_library_records(student_name, book_name)
  elif choice == "4":
    view_overdue_books()
  elif choice == "5":
    return
  else:
    print("Invalid choice.")



