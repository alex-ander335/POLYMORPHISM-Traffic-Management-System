#instance variable
class Student:
    def __init__(self):
        self.name = "name" #This is an instance variable. the difference is that class variables have the instance directly under the class without self.name
        self.age = "age"

    def display(self):
        print(f"Student name: {self.name}, age: {self.age}")

s1 = Student("Alexander")
s2 = Student("Zinale")
s3 = Student(22)
s1.display()
s2.display()
s3.display()