"""
	Here i am going to implement the classes that i have craeted so a far
"""

from SalaryEmp import Salaried_Employee
from CommissionedEmp import Commissioned_Employee
from Employee import Employee
from HourlyEmp import Hourly_Employee

emp1 = Salaried_Employee("Lukyamuzi","Benon","111-090-786",90000)
print(emp1.earnings())