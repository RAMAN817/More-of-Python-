#How to define a method with variable number of argument?
class test:
    def m1(self,a=None,b=None,c=None):
        if a is not None and b is not None and c is not None:
            print('Three Argument Method')
        
        elif a is  not None and b is not None:
            print('Two-Argument Method')
        
        elif a is not None:
            print('One-Argument Meethod')
        
        else:
            print('No-Argument method')

t= test()
t.m1()
t.m1(10)
t.m1(10,20)
t.m1(10,20,30)
#We are not requried to define mutliple method with different number 
#of argument .SO,We dont need the concept of method overloading.
