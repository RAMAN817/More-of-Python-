class Outer:
    def __init__(self):
        print('Outer Object Creation')
    
    class Inner:
        def __init__(self):
            print('Inner class object creattion...')

        def m1(self):
            print('Inner Class Method')

o= Outer()
i=o.Inner()
i.m1()

#or
# i = Outer().Inner()
# i.m1()          
