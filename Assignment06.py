# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Yuying Xie,5/27/2025, Adding Code
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
# student_first_name: str = ''  # Holds the first name of a student entered by the user.
# student_last_name: str = ''  # Holds the last name of a student entered by the user.
# course_name: str = ''  # Holds the name of a course entered by the user.
# student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
# file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

class FileProcessor:
    """ A collection of processing layer functions that work with Json files
        ChangeLog:
        Yuying Xie, 5.27.2025,Created Class
        Yuying Xie, 5.28.2025,Added functions
        Return: student data:list
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """This function work with Json files to load the data
            ChangeLog:
            Yuying Xie, 5.28.2025, Created function
            Return: None
        """
        try:
            file = open(FILE_NAME, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages("Text file must exist before running this script.", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """This function write the data into file
            ChangeLog:
            Yuying Xie, 5.28.2025, Created function
            Return: None
        """
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=4)
            file.close()
            last_data_saved = True
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            IO.output_error_messages("Please check that the file is not open by another program.", e)

class IO:
    """ A collection of presentation layer functions that manage user input and output
        ChangeLog:
        Yuying Xie, 5.27.2025,Created Class
        Yuying Xie, 5.28.2025,Added functions
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the custom error messages to the user
            ChangeLog:
            Yuying Xie, 5.28.2025, Created function
            return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("---Technical Error Message---")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """This function print out the menu
            ChangeLog:
            Yuying Xie, 5.28.2025, Created function
            Return: None
        """
        print()
        print(menu)
        print() # for user experience add space

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user
            ChangeLog:
            Yuying Xie, 5.28.2025, Created function
            Return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your choice: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Invalid choice")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def input_student_data(student_data:list):
        """ This function takes student data input from the user
            ChangeLog:
            Yuying Xie, 5.28.2025, Created function
            Return: student registered data
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers or space.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers or space.")
            if " " in student_first_name:
                raise ValueError("The first name should not contain numbers or space.")
            if " " in student_last_name:
                raise ValueError("The last name should not contain numbers or space.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}. Press 3 to save to file.")
        except ValueError as e:
            IO.output_error_messages("Please do not enter numbers or space.", e)
        except Exception as e:
            IO.output_error_messages("Non-specific errors.", e)
        return students

    @staticmethod
    def output_student_courses(student_data:list):
        """ This function process the data to create and display a custom message
            ChangeLog:
            Yuying Xie, 5.28.2025, Created function
            Return: student registered data
        """
        print("-" * 50)
        print("\nThe current data is:")
        for student in students:
            print(f'Student {student["FirstName"]} '
                f'{student["LastName"]} is enrolled in {student["CourseName"]}')

        print("-" * 50)


# Present and Process the data
students = FileProcessor.read_data_from_file(FILE_NAME, students)
while True:
    # Present the menu of choices
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data = students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data = students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")