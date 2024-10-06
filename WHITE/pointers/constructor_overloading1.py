# How to define a constructoe with variable number arguemnt
class Test:
    def __init__(self, a=None, b=None,c=None):
        print('COnstructor with 0/1/2/3')
t= Test()
t= Test(10)
t= Test(10,30)
t= Test(10,30,20)
