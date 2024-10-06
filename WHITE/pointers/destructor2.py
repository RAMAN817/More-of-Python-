#TO show that object is eligible for garbage collector once the reference varaible is removed
from time import *
class Test:
    def __init__(self):
        print('Constructor Executed')

    def __del__(self):
        print('Destructor Execution')
    
t1= Test()
t2= t1 #This means the object that t1 is refering is now also refer by t2
t3= t1 
del t1
sleep(10)
print('Object not destroyed after deleting t1')
del t2
sleep(10)
print('Obejct not destroyed after deleting t2')
print('Removing Last reference ')
del t3
print('End of Application')
