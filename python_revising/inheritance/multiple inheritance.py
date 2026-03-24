# Create multiple inheritance on teacher,student and youtuber.
# Q. if we have created teacher and now one student joins master degree with becoming teacher then what??
#
# Ans :  just make subclass from  teacher so that student will become teacher
# Now student is teacher as well as youtuber then what???
# -just use multiple inheritance for these three relations
from python_revising.inheritance.inheritance import Animal


class Teacher:
   def print_teacher(self):
       print("i can teach")


class Student:
    def print_student(self):
        print("is a student")

class Youtuber:
    def print_youtuber(self):
        print("can stream also")


class Person(Teacher, Student, Youtuber):
    pass


coder=Person()
coder.print_teacher()
coder.print_student()
coder.print_youtuber()