#It show how destrcutor works
import time
class destructor:
    def __init__(self) -> None:
        print('Initializing ')
    
    def __del__(self): #destructor
        print('The object is now  cleaning up ')

d= destructor()
d= None #Making it eligible for garbage collector 
time.sleep(10)
print('object cleaning sucessfully')