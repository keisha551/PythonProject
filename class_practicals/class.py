class NameClass:
    def _ _init_

    _(self, p1, p2):
    self.p1 = p1
    self.p2 = p2


def method1(self):
    ans = self.p1 * self.p2
    return ans


'''
inside def is the attribute and the methods are the behaviours
'''

x = NameClass(z,k)
x.p1 =z
x.p2 =k
x.method1()
x.method2()


class Student:
    # Contructor
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    # this function will just be printing
    def display_student_info(self):
        print(f"ID:,{self.student_id},Name:{self.name},Course:{self.course}")

    def update_course(self, new_course):
        self.course = new_course
        print(f"The updated course detail for student: {self.student_id}is{self.course}")


student1 = student(100, "Simon", "Software Development")
student2 = student(101, "Keisha", "Cybersecurity")

student1.display_student_info()
student1.update_course("Cyber Security")

student1.display_student_info()

print(student1.student_id)