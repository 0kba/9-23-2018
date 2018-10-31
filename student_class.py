class Student:
	def __init__(self, firstname, lastname, gradeLevel):
             self.firstname = firstname
             self.lastname = lastname
             self.grade_level = gradeLevel
	
	def get_whole_name(self):
		return f"{self.lastname}, {self.firstname}"


studentA = Student('Abdo', 'Ali', 5)
print(studentA.get_whole_name())
