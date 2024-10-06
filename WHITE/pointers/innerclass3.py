class Person:
    def __init__(self,name,dd,mm,yyyy):
        print('Person Object Creation')
        self.name= name
        self.dob= self.Dob(dd,mm,yyyy)

    def info(self):
        print('Name:',self.name)
        self.dob.display()
    
    class Dob:
        def __init__(self,dd,mm,yyyy):
            print('Dob Object Creation')
            self.dd= dd
            self.mm= mm
            self.yyyy= yyyy
        
        def display(self):
            print('Dob-{}/{}/{}'.format(self.dd,self.mm,self.yyyy))

p= Person('roman',28,4,2004)
p.info()

    
