#If there is no naming cocflict then self is also ok.
class P:
    a= 10
    def __init__(self):
        print('Parent Class Constructor')

    def m1(self):
        print('Parent Instance Class')
    
    @classmethod
    def m2(cls):
        print('Parent Class Instance')
    
    @staticmethod
    def m3(): 
        print('Parent static Method')
    
class C(P):
    def __init__(self):
            print('Child Constructor')
        
    def method1(self):
            print(super().a)
            super().m1()
            super().m2()
            super().m3()
            super().__init__()#Self cant be used here.
        

c= C()
c.method1()
