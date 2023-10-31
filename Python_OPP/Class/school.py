class Student():
    def __init__(self, name, classes, id):
        self.name = name
        self.id = id
        self.classes = classes
    
    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.classes}, id: {self.id}'
    


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = subject

    def __repr__(self) -> str:
        return f'Student with name: {self.name}, Subjet: {self.subject}, id: {self.id}'
    

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []


    def add_teacher(self, name, subject):
        id = len(self.teachers)+100
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee<6500:
            return 'Not Enough fee'
        else:
            id = len(self.students)+1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id {id}, extra money {fee - 6500}'

    def __repr__(self) -> str:
        print('Welcome to ,', self.name)
        print('----------Our Teachers----------')
        for teacher in self.teachers:
            print(teacher)

        print('--------Our Student')
        for student in self.students:
            print(student)


# alia = Student("Alia Buth", 9, 1)
# print(alia)
# ranbeer = Teacher('Douren Been', 'Algorithm', 101)
# print(ranbeer)

phitron = School('Phitrons')

phitron.enroll('Ali', 5200)
phitron.enroll('Aishwaraiya', 8000)
phitron.enroll('Viajna', 90000)

phitron.add_teacher('Corss','DS' )
phitron.add_teacher('Decaps','AL' )


print(phitron)