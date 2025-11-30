import time
import os

name = input("Enter your name: ").capitalize()
print()
time.sleep(2)
print(f"Welcome to system professor {name}\nPlease follow instructions")
time.sleep(3)


class Students:
    def __init__(self, name: str, roll_number: int, grade: str):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade.upper()

    def display(self):
        print(f"Roll Number: {self.roll_number}, Name: {self.name}, Grade: {self.grade}")

    def file_to(self):
        return f"{self.name},{self.roll_number},{self.grade}\n"

    @staticmethod
    def file_from(line):
        name, roll_number, grade = line.strip().split(",")
        return Students(name, int(roll_number), grade)


class Student_System:
    name = "students.txt"

    def soft(self):
        while True:
            self.show_menu()
            try:
                option = int(input("Choose option: "))
            except ValueError:
                print(" Please enter a number.")
                continue

            if option == 1:
                self.add_student()
            elif option == 2:
                self.view_all_students()
            elif option == 3:
                self.search_student_by_roll_number()
            elif option == 4:
                self.update_student_grade()
            elif option == 5:
                print("SOFT ENDED")
                break
            else:
                print("Invalid option.")
  

    def show_menu(self):
        print("Students List Control System\n")
        print("1-Add student\n2-View students list\n3-Find student by roll number\n4-Update student's grade\n5-Exit")
     
   
    def add_student(self):
        name = input("Input student name: ")
        roll_number = int(input("Input student roll number: "))
        grade = input("Input grade from (A-B): ").upper()

        if os.path.isfile(self.name):
            with open(self.name, 'r') as file:
                lines = file.readlines()
                for line in lines[1:]:
                    student = Students.file_from(line)
                    if student.roll_number == roll_number:
                        print(f"Roll number {roll_number} is already taken.")
                        return 

        student = Students(name, roll_number, grade)
        
            
        
        file_exists = os.path.isfile(self.name)

        with open(self.name, "a") as file:
            if not file_exists:
                file.write("Name,Roll Number,Grade\n")
            file.write(student.file_to())

        print("Student added to list.")

   
    def view_all_students(self):
        if not os.path.isfile(self.name):
            print("Students file not found.")
            return

        with open(self.name, "r") as file:
            lines = file.readlines()

       
        print("\n--- Students List ---")
        for line in lines[1:]: 
            student = Students.file_from(line)
            student.display()

    
    def search_student_by_roll_number(self):
        if not os.path.isfile(self.name):
            print("Students file not found.")
            return

        roll_number = input("Enter the roll number: ")
        found = False

        with open(self.name, "r") as file:
            lines = file.readlines()

            for line in lines[1:]:
                student = Students.file_from(line)
                if str(student.roll_number) == roll_number:
                    print("\nStudent found:")
                    student.display()
                    found = True
                    break

        if not found:
            print("Student not found.")

   
    def update_student_grade(self):
        if not os.path.isfile(self.name):
            print("Students file not found.")
            return

        roll_number = input("Enter the roll number: ")
        new_grade = input("Enter new grade from (A-B): ").upper()

        with open(self.name, "r") as file:
            lines = file.readlines()

      

        with open(self.name, "w") as file:
            file.write(lines[0]) 

            for line in lines[1:]:
                student = Students.file_from(line)
                if str(student.roll_number) == roll_number:
                    student.grade = new_grade
                    
                file.write(student.file_to())

       


run = Student_System()
run.soft()

 

