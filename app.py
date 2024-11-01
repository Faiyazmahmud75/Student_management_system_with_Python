from students import Student
from courses import Course
import json

class SystemManagement:
    def __init__(self):
        self.students = {}
        self.courses = {}

# Menu-01. Add New Student
    def add_new_student(self):
        name = input("Enter Student's Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ").upper()

        if student_id in self.students:
            print(f"Student (ID {student_id}) already exists")
        else:
            new_student = Student(name, age, address, student_id)
            self.students[student_id] = new_student
            print(f"Student {name} (ID: {student_id}) added successfully.")


# Menu-02. Add New Course
    def add_new_course(self):
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ").upper()
        course_instructor = input("Enter Instructor Name: ")

        if course_code in self.courses:
            print(f"Course Code ({course_code}) already exists!")
        else:
            new_course = Course(course_name, course_code, course_instructor)
            self.courses[course_code] = new_course
            print(f"Course {course_name} (Code: {course_code}) created with instructor {course_instructor}")

# Menu-03. Enroll Student in Course
    def course_enroll(self):
        course_student_id = input("Enter Student ID: ").upper()
        enroll_course_code = input("Enter Course Code: ").upper()

        if course_student_id not in self.students:
            print(f"Student ID({course_student_id}) not found")
            return
        if enroll_course_code not in self.courses:
            print(f"Course Code({enroll_course_code}) not found")
            return

        student = self.students[course_student_id]
        course = self.courses[enroll_course_code]

        course.add_student(student)
        student.course_enroll(course.course_code)


# Menu-04. Add Grade
    def add_grade(self,):
        student_id_for_grade = input("Enter Student ID: ").upper()
        course_code_for_grade = input("Enter Course Code: ").upper()
        grade = input("Enter Grade: ").upper()

        if course_code_for_grade not in self.courses:
            print("Invalid Course Code. This Course doesn't exist")
        elif student_id_for_grade not in self.students:
            print("Invalid Student ID. No student found with the given ID")
        else:
            course_name_for_grade = self.courses[course_code_for_grade].course_name
            self.students[student_id_for_grade].add_grade(course_code_for_grade, grade, course_name_for_grade )


# Menu-05. Display Student info
    def display_student_info(self):
        student_id = input("Enter Student ID: ").upper()
        if student_id in self.students:
            self.students[student_id].display_student_info()
        else:
            print(f"Student ID({student_id}) not found.")


# Menu-06 Display Course info
    def display_course_info(self):
        course_code = input("Enter Course Code: ").upper()
        if course_code in self.courses:
            self.courses[course_code].display_course_info()
        else:
            print(f"Course Code ({course_code}) not found.")

# Menu-07 Save Data
    def save_data(self, filename='system_data.json'):
        data = {
            "students": {student_id: student.to_dict() for student_id, student in self.students.items()},
            "courses": {course_code: course.to_dict() for course_code, course in self.courses.items()}
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("All student and course data saved successfully.")


# Menu-08 Load Data
    def load_data(self, filename='system_data.json'):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"No file found with the name {filename}. Starting with an empty system.")
            return

        self.students = {
            student_id: Student(**student_data)
            for student_id, student_data in data.get("students", {}).items()
        }
        self.courses = {}
        for course_code, course_data in data.get("courses", {}).items():
            course = Course(
                course_name=course_data["course_name"],
                course_code=course_code,
                instructor=course_data["instructor"]
            )
            self.courses[course_code] = course

            for student_id in course_data["students"]:
                if student_id in self.students:
                    student = self.students[student_id]
                    course.add_student(student)
                    student.course_enroll(course.course_code)





    def run(self):
        while True:
            print("""
==== Student Management System ====
1. Add New Student
2. Add New Course
3. Enroll Student in course
4. Add Grade for Student
5. Display Student Details
6. Display Course Details
7. Save Data to File
8. Load Data from File
0. Exit
""")
# operation = None
            user_input = input("Select Option: ")
            if user_input == "1":
                self.add_new_student()
            elif user_input == "2":
                self.add_new_course()
            elif user_input == "3":
                self.course_enroll()
            elif user_input == "4":
                 self.add_grade()
            elif user_input == "5":
                self.display_student_info()
            elif user_input == "6":
                self.display_course_info()
            elif user_input == "7":
                self.save_data()
            elif user_input == "8":
                self.load_data()
            elif user_input == "0":
                print("====Exiting Student Management System. Goodbye!====")
                break
            else:
                print("invalid input! Choose an option between 0 and 8")

system = SystemManagement()
system.run()