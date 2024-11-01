class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student to DB")

s1 = Student("Rakesh", 76)
print(s1.name, s1.marks)

s2 = Student("Arjun", 97)
print(s2.name, s2.marks)

