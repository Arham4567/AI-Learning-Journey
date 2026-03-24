# Create a custom exception AdultException.
#
# Create a class Person with attributes name and age in it.
#
# Create a function get_minor_age() in the class. It throws an exception if the person is adult otherwise returns age.
#
# Create a function display_person() which prints the age and name of a person.
#
# let us say,
#
# if age>18
#     he is major
# else
#     raise exception
#
# create cusomException named ismajor and raise it if age<18.

class Person:
    def __init__(self):
        self.age = None
        self.name = None

    def get_minor_age(self) -> int | None:
        self.name = input("Enter your name")
        self.age = int(input("Enter your age"))
        try:
            if self.age > 18:
                raise ValueError("You are an Adult")
        except ValueError as e:
            print(f"{e}")

        else:
            return self.age

    def display_person(self):
            print("my name is",self.name)
            print("my age is",self.age)


p1=Person()
p1.get_minor_age()
p1.display_person()