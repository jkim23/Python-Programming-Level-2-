#JT KIM
#4/30/19
#creating a method that prints a greeting

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def myfunc(self):
        print("Welcome " + self.name) 

p1 = Student("John", "Computer Science")
p1.myfunc()

print(p1.name)
print(p1.major)

    
