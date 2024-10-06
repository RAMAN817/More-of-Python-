class Person:
    def __init__(self,name,age,weight,height):
        self.name= name
        self.age= age
        self.weight= weight
        self.height= height

    def display(self):
        print('Name',self.name)
        print('Age',self.age)
        print('Height',self.height)
        print('Weight',self.weight)


class Employee(Person):
    def __init__(self,name,age,weight,height,eno,esal):
        super().__init__(name,age,weight,height)
        self.eno= eno
        self.esal= esal
    
    def display(self):
        super().display()
        print('Eno',self.eno)
        print('Esal',self.esal)
e= Employee('Roman',19,60,5.7,872425,2115201)       
e.display()