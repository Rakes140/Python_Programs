class Student:
    college_name = "OUTR"

    # parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    # method creation and calling
    def welcome(self):
        print("welcome student")

    def get_marks(self):
        return self.marks
    

s1 = Student("Rakesh", 76)
s1.welcome()
print(s1.get_marks())
