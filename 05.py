class Employee:
    def __init__(self,name,empID):
        self.name = name
        self.empID = empID
    
empName = input("Name: ")
empID = input("EmpID: ")

theEmployee = Employee(empName, empID)

print(f"The name is {theEmployee.name} of {theEmployee.empID} " )