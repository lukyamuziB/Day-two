from Employee import Employee
class Commissioned_Employee(object):
	"""docstring for Commissioned_Employee"""
	def __init__(self,first_name,last_name,social_security_number, gross_sales, rate):
	
		if gross_sales < 0.0:
			raise ValueError("Gross sales cant be less than 0")
		if rate < 0.0:
			raise ValueError("rate sales cant be less than 0")
		self._first_name = first_name
		self._last_name = last_name
		self._social_security_number = social_security_number
		self._gross_sales = gross_sales
		self._rate = rate

	def get_gross(self , gross):
		if gross_sales < 0.0:
			raise ValueError("Gross sales cant be less than 0")
		self._gross_sales = gross
	def get_gross(self):
		return self._gross_sales

	def set_rate(self , rate):
		if rate < 0.0:
			raise ValueError("rate sales cant be less than 0")
		self._rate = rate
	def get_rate(self):
		return self._rate
		
	def earnings(self):
		return self._gross_sales * self._rate
	def report(self):
		a = Commissioned_Employee.earnings(self)
		print("First Name: %s\nLast Name: %s\nSocial Number: %s\nGross Sales: %.3f\nCommission Rate: %.3f\nEarns: %.3f\n"%(self._first_name,self._last_name,self._social_security_number,self._gross_sales,self._rate,a))


