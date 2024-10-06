#To show that Child class has everything that parent have
class P:
    a= 10
    def __init__(self):
        print('Parent Constructor')
        self.b= 20
    
    def m1(self):
        print('Parent Instance Method')
    
    @classmethod
    def m2(self):
        print('Parent Class Method')
    
    @staticmethod
    def m3():
        print('Parent static method')
class C(P):
    pass
c=C() #Class C has nothing so when we call child class it will call parnet classs 
c.m2()
c.m1()
c.m3()
print(c.a)
print(c.b)