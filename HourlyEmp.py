from Employee import Employee
class Hourly_Employee(Employee):
	def __init__(self,first_name,last_name,social_security_number, wage, hours):
		# super(Hourly_Employee, self).__init__()
		if wage <= 0:
			raise ValueError("Wage must be greater than zero")
		if((hours < 0.0) or (hours > 168.0)):
			raise ValueError("Hours worked must be between 0 and 168")
		self._first_name = first_name
		self._last_name = last_name
		self._social_security_number = social_security_number
		self._wage = wage
		self._hours = hours
		

	def setWage(self, ammount):
		if wage <= 0:
			raise ValueError("Wage must be greater than zero")
		self._wage = ammount
	def get_wage(self, ammount):
		return self._wage

	def set_hours_worked(self, hrs):
		if((hours < 0.0) or (hours > 168.0)):
			raise ValueError("Hours worked must be between 0 and 168")
		this._hours= hrs

	def get_hours_worked(self):
		return self._hours

	def earnings(self):
		if self._hours< 40:
			return self._hours * self._wage
		#employess that work over time get a bonus of 3.5 per hour
		return (self._hours * self._wage) + ((self._hours-40) * 3.5)
	def report(self):
		earns = Hourly_Employee.earnings(self)
		print("First Name: %s\nLast Name: %s\nSocial Number: %s\nWage: %f\nHours Worked: %f\nEarns: %f\n"%(self._first_name,self._last_name,self._social_security_number,self._wage,self._hours,earns))