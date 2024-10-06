#How to define a variable length argument in Constructor
class  Test:
    def __init__(self,*args):
        print('Constructor with Variable no of Argument')
t= Test()
t=Test(10,20)
t= Test(10,20,30)
t= Test(10,20,30,40)
