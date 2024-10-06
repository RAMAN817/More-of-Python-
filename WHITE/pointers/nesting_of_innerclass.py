class Outer:
    def __init__(self):
        print('Outer class Object Creation')
    
    class Inner:
        def __init__(self) -> None:
            print('Inner class Object Creation')
    
        class NestedInner:
            def __init__(self) -> None:
               print('NestedInner class Object Creation')
            
            def m1(self):
                print('SELF nested inner')

o= Outer()
i= o.Inner()
ii= i.NestedInner()
ii.m1()

#or
#Outer().Inner().InnerInner().m1()
         