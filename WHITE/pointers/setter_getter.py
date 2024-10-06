#if you dont know data then go for setter and getter method.
class student:
    def setName(self,name):
        self.name= name
    
    def getName(self):
        return self.name
    
    def setMarks(self,marks):
        self.marks= marks
    
    def getMarks(self):
        return self.marks

n= int(input('Enter the Number of student'))
students=[]
for i in range(n):
    s= student()
    name= input('Enter Your Name')
    marks= input('Enter Your Marks')
    s.setName(name)
    s.setMarks(marks)
    students.append(s)

for s in students:
    print('Hi',s.getName())
    print('Your Marks are:',s.getMarks())
    print()
    