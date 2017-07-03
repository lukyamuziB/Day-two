from Employee import Employee
class Salaried_Employee(Employee):
	"""docstring for Salaried_Employee"""
	def __init__(self,first_name,last_name,social_security_number, weekly_salary):
		super(Employee, self).__init__()
		if weekly_salary < 0.0:
			raise ValueError("Sorry, weekly salary cant be less than 0")
		self._weekly_salary = weekly_salary

	def set_salary(self, ammount):
		if ammount < 0.0:
			raise ValueError("Sorry, weekly salary cant be less than 0")
	def get_salary(self):
		return self._weekly_salary

	def earnings(self):
		return self._weekly_salary*4

