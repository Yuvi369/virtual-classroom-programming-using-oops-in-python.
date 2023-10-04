class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.assignments = []
        self.teacher=[]

    def add_teacher(self,teacher):
        self.teacher.append(teacher)

    def list_teachers(self):
        return self.teacher
        
    def add_student(self, student):
        self.students.append(student)

    def list_students(self):
        return self.students

    def schedule_assignment(self, assignment):
        self.assignments.append(assignment)

    def list_assignments(self):
        return self.assignments

class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class Assignment:
    def __init__(self, assignment_name, due_date):
        self.assignment_name = assignment_name
        self.due_date = due_date


class VirtualClassroomManager:
    def __init__(self):
        self.classrooms = {}

    def add_classroom(self, name):
        self.classrooms[name] = Classroom(name)
        print(f"Classroom '{name}' has been created.")

    def add_teacher(self, teacher_id, classroom_name, teacher_name):
        if classroom_name in self.classrooms:
            teacher=Teacher(teacher_id,teacher_name)
            self.classrooms[classroom_name].add_teacher(teacher)
            print(f"Teacher {teacher_id} has been enrolled in {classroom_name}.")
        else:
            print(f"Classroom '{classroom_name}' does not exist.")

    def add_student(self, student_id, classroom_name, student_name):
        if classroom_name in self.classrooms:
            student = Student(student_id, student_name)
            self.classrooms[classroom_name].add_student(student)
            print(f"Student {student_id} has been enrolled in {classroom_name}.")
        else:
            print(f"Classroom '{classroom_name}' does not exist.")

    def schedule_assignment(self, classroom_name, assignment_name, due_date):
        if classroom_name in self.classrooms:
            assignment = Assignment(assignment_name, due_date)
            self.classrooms[classroom_name].schedule_assignment(assignment)
            print(f"Assignment for {classroom_name} has been scheduled.")
        else:
            print(f"Classroom '{classroom_name}' does not exist.")

    def submit_assignment(self, student_id, classroom_name, assignment_name):
        if classroom_name in self.classrooms:
            classroom = self.classrooms[classroom_name]
            for student in classroom.list_students():
                if student.student_id == student_id:
                    for assignment in classroom.list_assignments():
                        if assignment.assignment_name == assignment_name:
                            print(f"Assignment submitted by Student {student_id} in {classroom_name}.")
                            return
                    print(f"Assignment '{assignment_name}' does not exist in {classroom_name}.")
                    return
            print(f"Student {student_id} is not enrolled in {classroom_name}.")
        else:
            print(f"Classroom '{classroom_name}' does not exist.")


# Initialize the manager
manager = VirtualClassroomManager()

while True:
    # Get user input
    command = input("Enter a command 1.add_classroom, 2.add_teacher, 3.add_student, 4.schedule_assignment, 5.submit_assignment, 6.exit): ").strip()

    if command == "exit":
        break
    elif command == "add_classroom":
        classroom_name = input("Enter classroom name: ").strip()
        manager.add_classroom(classroom_name)
    elif command=="add_teacher":
        teacher_id=int(input("Enter teacher ID: "))
        teacher_name = input("Enter teacher name: ").strip()
        manager.add_teacher(teacher_id, classroom_name, teacher_name)
    elif command == "add_student":
        student_id = int(input("Enter student ID: "))
        classroom_name = input("Enter classroom name: ").strip()
        student_name = input("Enter student name: ").strip()
        manager.add_student(student_id, classroom_name, student_name)
    elif command == "schedule_assignment":
        classroom_name = input("Enter classroom name: ").strip()
        assignment_name = input("Enter assignment name: ").strip()
        due_date = input("Enter due date: ").strip()
        manager.schedule_assignment(classroom_name, assignment_name, due_date)
    elif command == "submit_assignment":
        student_id = int(input("Enter student ID: "))
        classroom_name = input("Enter classroom name: ").strip()
        assignment_name = input("Enter assignment name: ").strip()
        manager.submit_assignment(student_id, classroom_name, assignment_name)
    else:
        print("Invalid command. Please try again.")
