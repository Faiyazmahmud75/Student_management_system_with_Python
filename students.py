from logging import exception
class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


class Student(Person):
    def __init__(self, name, age, address, student_id, grades=None, courses=None):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = grades if grades is not None else {}
        self.courses = courses if courses is not None else []

    def add_grade(self, subject, grade, course_name):
        if grade not in ['A', 'B', 'C', 'D', 'F']:
            print("Invalid Grade")
        elif subject not in self.courses:
            print("Student doesn't enrolled this course")
        else:
            try:
                self.grades[subject] = grade
                print(f"Grade {grade} added for {self.name} in {course_name}")
            except Exception as e:
                print("Error!", e)

    def course_enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def display_student_info(self):
        self.display_person_info()
        print(f"Student ID: {self.student_id}")
        print(f"Enrolled Courses: {', '.join(self.courses) if self.courses else 'No Course Enrolled'}")
        print(f"Grades: {self.grades if self.grades else 'None'}")

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "address": self.address,
            "student_id": self.student_id,
            "grades": self.grades,
            "courses": self.courses
        }