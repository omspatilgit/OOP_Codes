# Student Management System using OOP

class Student:

    # Constructor - Automatically called when an object is created
    def __init__(self):
        self.name = ""
        self.roll = 0
        self.div = ""
        self.marks = 0

    # Method to take student details from the user
    def get_std_info(self):
        self.name = input("Enter Student Name :: ")
        self.roll = int(input("Enter Student Roll no :: "))
        self.div = input("Enter Student Div :: ")

        # Validate marks (0 to 100)
        while True:
            self.marks = int(input("Enter The Student Marks :: "))

            if self.marks > 100 or self.marks < 0:
                print("Invalid Marks!!!")
            else:
                break

    # Method to display student details
    def std_detail_display(self):

        # Check whether student details have been entered
        if self.name == "":
            print("Please enter student details first.")
            return

        print(f"\nStudent Name      : {self.name}")
        print(f"Student Roll No   : {self.roll}")
        print(f"Student Division  : {self.div}")
        print(f"Student Marks     : {self.marks}")

    # Method to display student's grade
    def std_grade_info(self):

        # Check whether student details have been entered
        if self.name == "":
            print("Please enter student details first.")
            return

        print(f"\nStudent Total Marks : {self.marks}")

        # Determine grade based on marks
        if self.marks >= 90:
            print("Grade : A+")
        elif self.marks >= 80:
            print("Grade : A")
        elif self.marks >= 70:
            print("Grade : B")
        elif self.marks >= 60:
            print("Grade : C")
        else:
            print("Grade : Fail")


# ---------------- Driver Code ----------------

# Create Student object
obj = Student()

# Run menu continuously until user exits
while True:

    print("\n----------- Student Management -----------")
    print("1. Enter Student Details")
    print("2. Display Student Details")
    print("3. Show Grade")
    print("4. Exit")

    # Take user's menu choice
    choice = int(input("Enter Your Choice :: "))

    # Perform operation based on user's choice
    if choice == 1:
        obj.get_std_info()

    elif choice == 2:
        obj.std_detail_display()

    elif choice == 3:
        obj.std_grade_info()

    elif choice == 4:
        print("Bye...")
        break

    # Invalid menu option
    else:
        print("Invalid Choice")