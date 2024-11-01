from students import Student
class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.course_students = []

    def add_student(self, student):
        if isinstance(student, Student):
            if student not in self.course_students:
                self.course_students.append(student)
                print(f"Student {student.name} (ID {student.student_id}) successfully enrolled in Course ({self.course_code})")
            else:
                print("Student is already enrolled in this course.")
        else:
            print("Student not found! Please add student first.")


    def display_course_info(self):
        print(f"Course: {self.course_name},\nCourse Code: {self.course_code},\nInstructor: {self.instructor}")
        print("Enrolled Students:")
        for student in self.course_students:
            print(student.name)

    def to_dict(self):
        return {
            "course_name": self.course_name,
            "course_code": self.course_code,
            "instructor": self.instructor,
            "students": [student.student_id for student in self.course_students]  # Store only student IDs
        }