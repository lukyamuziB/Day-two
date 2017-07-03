from Employee import Employee
class Commissioned_Employee(object):
	"""docstring for Commissioned_Employee"""
	def __init__(self,first_name,last_name,social_security_number, gross_sales, rate):
		super(Commissioned_Employee, self).__init__()
		if gross_sales < 0.0:
			raise ValueError("Gross sales cant be less than 0")
		if rate < 0.0:
			raise ValueError("rate sales cant be less than 0")

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
		
	def earnings():
		return get_rate() * get_gross()


