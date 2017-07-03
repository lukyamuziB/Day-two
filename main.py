"""
	Here i am going to implement the classes that i have craeted so a far
"""

from SalaryEmp import Salaried_Employee
from CommissionedEmp import Commissioned_Employee
from Employee import Employee
from HourlyEmp import Hourly_Employee

emp1 = Salaried_Employee("lukya","bahb","busBD",90000)
print(emp1.earnings())

print(emp1.get_last_name())
emp1.report()

emp2 = Commissioned_Employee("nak","kak","908-984-565",12.09,78.1)

print(emp2.earnings())

emp3 = Hourly_Employee("Alexis","Sanchez","103-908-675",7000,140)

Employees = []
Employees.append(emp1)
Employees.append(emp2)
Employees.append(emp3)

for emp in Employees:
	emp.report()
	if  isinstance(emp, Commissioned_Employee):
		emp.set_rate(20.78)
		print("New earnings of the Commissioned Employed are: %f"%emp.earnings())
