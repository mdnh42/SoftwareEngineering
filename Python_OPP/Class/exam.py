class Exam():

    def __init__(self, getMarks):
        self.getMarks = getMarks
        self.min_marks = 33
        self.max_marks = 100

    def pass_student(self, marks):
        if(marks>=33 and marks<=100):
            print(f'Pass {marks}')
        else:
            print(F'Fail {marks}')



Akib = Exam("Akib")

Akib.pass_student(30)
Akib.pass_student(33)