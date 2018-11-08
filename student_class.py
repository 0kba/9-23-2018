class Student:
    def __init__(self, firstname, lastname, gradeLevel):
        self.firstname = firstname
        self.lastname = lastname
        self.grade_level = gradeLevel

    def display(self):
        print(f"{self.lastname}, {self.firstname}  " , self.grade_level)

    # def get_whole_name(self):
    #     return f"{self.lastname}, {self.firstname}"


d = Student('Abdo', 'Ali', 544), Student('Ab', 'Al', 544),Student('A', 'A', 533),Student('Abd', 'f', 54)


for i in d:
    print(i.display())

