class Student:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def details(self):
        return f"I am {self.name} and {self.age} old student."

class Course:
    def __init__(self,name,max_student):
        self.name = name
        self.max_student = max_student
        self.students = []
    def add_student(self,student):
        if len(self.students) < self.max_student:
            self.students.append(student.name)
            return True
        print( "Course is Full")

s1 = Student("Bikramjeet",18)
s2 = Student("Ankit",20)
s3 = Student("Ravi",17)

myCourse = Course("Cpp",2)
myCourse.add_student(s1)
myCourse.add_student(s2)
myCourse.add_student(s3)

print(myCourse.students)
