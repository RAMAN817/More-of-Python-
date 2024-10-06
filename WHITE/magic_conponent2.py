#Program to overload multiplication operator 
class Employee:
    def __init__(self,ename,salaryPerDay):
        self.name= ename
        self.salaryPerDay= salaryPerDay
    def __mul__(self,other):
       return self.salaryPerDay*other.workingDays




class TimeSheet:
    def __init__(self,name,workingDays):
        self.name= name
        self.workingDays= workingDays

e= Employee('Roman',75)
t= TimeSheet('Roman',30)
print('The salary Of this Month is ',e*t)
#e is first argument so python will call magic method from first argument class.