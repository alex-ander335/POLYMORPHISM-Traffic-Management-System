class Student:
    def __init__(self):
        self.name = "UMaT" #This is an instance variable. the difference is that class variables have the instance directly under the class without self.name
        self.age = 18

s1 = Student()
s2 = Student()
print(s1.name)
print(s2.age)

