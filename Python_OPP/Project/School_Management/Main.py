from School import School, ClassRoom, Subject
from Persons import Student, Teacher
def main():
    school = School('Adam Jee U To', 'Dhaka')


    # add Students
    eight = ClassRoom('Eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    abul = Student('Abir Khan', eight)
    school.student_admission(abul)

    babul = Student('babul Khan', eight)
    school.student_admission(babul)
    cabul = Student('cabul Khan', eight)
    school.student_admission(cabul)


    # subjects 
    physic_teacher= Teacher('Shajahan Topon Rana')
    physic = Subject('physics', physic_teacher)
    eight.add_student(physic)


    print(school)

if __name__ == '__main__':
    main()

