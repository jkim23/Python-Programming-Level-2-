#JT KIM
#4/30/19
#modifying object properties

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def myfunc(self):
        print("Welcome " + self.name) 

p1 = Student("John", "Computer Science")
p1.myfunc()

p1.major = "Accounting"

print(p1.name)
print(p1.major)

    
