import random 
class Person:
    def __init__(self, name) -> None:
        self.name = name




class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.subject = subject

    def teach(self):
        pass

    def __repr__(self) -> str:
        return f'{self.name}'
    

    def take_exam(self, subject, students):
        for student in students:
            marks =  random.randint(0, 100)
            # TODO: set marks for the subject for each subject 


class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.id = None
        self.subjects = []
        self.marks = {}
        self.grade = None

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value