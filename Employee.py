from abc import ABC, abstractmethod
class Employee(ABC):
	"""docstring for Employee"""
	def __init__(self, first_name, last_name, social_security_number):
		self._first_name = first_name
		self._last_name = last_name
		self._social_security_number = social_security_number
		#super(AbstractOperation, self).__init__()

	def get_first_Name(self):
		return self._first_name
	def get_last_Name(self):
		return self._last_name
	def get_social_number(self):
		return self._social_security_number

	@abstractmethod
	def earnings(self):
		pass


		