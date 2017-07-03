from Employee import Employee
class Hourly_Employee(Employee):
	def __init__(self,first_name,last_name,social_security_number, wage, hours):
		super(Employee, self).__init__()
		if wage <= 0:
			raise ValueError("Wage must be greater than zero")
		if((hours < 0.0) or (hours > 168.0)):
			raise ValueError("Hours worked must be between 0 and 168")
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
		if get_hours_worked()< 40:
			return get_hours_worked() * get_wage()
		#employess that work over time get a bonus of 3.5 per hour
		return (get_hours_worked() * get_wage()) + ((get_hours_worked()-40) * 3.5)



		