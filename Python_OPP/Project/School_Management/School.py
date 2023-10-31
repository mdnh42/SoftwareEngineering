class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        #composition 
        self.classroom = {}
 
    def add_classroom(self, classroom):
        self.classroom[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student, classroom):
        className = student.classroom.name
        if classroom in self.classroom:
            #TODO: set student id, (roll num) at the time of adding the student 
            self.classroom[classroom.name].add_student(student)
        else:
            print(f'No Classroom as named{className}')
    def __repr__(self) -> str:
        print('--------All Class Rooms-------')
        for key, value in self.classroom.items():
            print(key)
        
        print('---------Studnets----------')
        eight = self.classroom['eight']
        print(len(eight.students))

        return ''

class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name 
        # composition 
        self.students = []
        self.subjects = []
        

    def add_student(self, student):
       serial_id = f'{self.name} - {len(self.students) + 1}'
       student.id = serial_id
       student.classroom = self.name
       self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'
    

    #TODO sort students by grade
    def get_top_student(self):
        pass


class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 30

