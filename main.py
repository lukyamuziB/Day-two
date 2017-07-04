"""
	Here i am going to implement the classes that i have craeted so a far
	Then  create an array of the instances of the classes
	Iterate through themm and increase the earnings of the Commissioned Employees using polymmophism
"""

from SalaryEmp import Salaried_Employee
from CommissionedEmp import Commissioned_Employee
from HourlyEmp import Hourly_Employee

try:

	emp1 = Salaried_Employee("lukya", "bahb", "busBD", 90000)
	emp2 = Commissioned_Employee("nak","kak","908-984-565",12.09,78.1)
	emp3 = Hourly_Employee("Alexis", "Sanchez", "103-908-675", 7000, 140)
except ValueError as e:
	print("Adjust your working values to get everything right")

employees = []
employees.append(emp1)
employees.append(emp2)
employees.append(emp3)

for emp in employees:
	emp.report()
	if  isinstance(emp, Commissioned_Employee):
		emp.set_rate(20.78)
		print("New earnings of the Commissioned Employed are: %.3f"%emp.earnings())
