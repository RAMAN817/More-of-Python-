#Accessing Member of one class inside another class
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno= eno
        self.ename= ename
        self.esal= esal

    def display(self):
        print('Employee Name:',self.ename) 
        print('Employee No',self.eno)
        print('Employee Salary',self.esal)
    
class Manager:
    #this is a static method look carefully
    def updateEmpSalary(emp):
        emp.esal= emp.esal+10000
        emp.display()

emp= Employee(101,'Roman',45000)
Manager.updateEmpSalary(emp)