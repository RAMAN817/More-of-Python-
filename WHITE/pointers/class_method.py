#Program to track number of oibject created for a class:
class test:
    count= 0
    def __init__(self):
        test.count=test.count + 1

    @classmethod
    def getNoofObject(cls):
        print('The No of object created',test.count)
    
test.getNoofObject()
t1=test()
t2=test()
t3=test()
t4=test()
test.getNoofObject()