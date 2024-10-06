#To show IS_A_relationdhip with person class and employee class
class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
    
    def eatndrink(self):
        print('Eating Biryani and Drinking Beer')
    
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        #self.name= name
        #self.age= age
        #You can do that but there is already same construcor is  in parent class so to call it
        super().__init__(name,age)
        self.eno= eno
        self.esal= esal
    
    def work(self):
        print('Coding Python Programs')
    
    def empinfo(self):
       print('Employee Name:',self.name) 
       print('Employee Age',self.age)
       print('Employee Nukber',self.eno)
       print('Employee Salary',self.esal)

e= Employee('Romanson Thapa',19,872425,100000)
e.eatndrink()
e.work()
e.empinfo()


