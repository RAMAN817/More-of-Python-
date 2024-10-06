class Person:
    def __init__(self,name,age,height,weight):
        self.name= name
        self.age= age
        self.height= height
        self.weight= weight
    
    def display(self):
        print('Name ',self.name)
        print('Age',self.age)
        print('Height',self.height)
        print('Weight',self.weight)
    
class Student(Person):
    def __init__(self,name,age,height,weight,rollno,marks):
        super().__init__(name,age,height,weight)
#Super is comppulsary you cant use self 
        self.rollno= rollno
        self.marks= marks

    def display(self):
        super().display()
        print('ROll no',self.rollno)
        print('Marks',self.marks)

s= Student('ROMAN',19,5.7,54,744,100)
s.display()