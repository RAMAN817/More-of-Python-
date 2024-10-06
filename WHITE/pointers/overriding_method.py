class parent :
    def property(self):
        print('Land+gold+cash+ Connections')
    
    def marry(self):
        print('Manisha') #Overridden method

class child(parent):
    def marry(self):
        print('Mia Melona') #overriding method

c= child()
c.property()
c.marry()
#if you want both you have to use super function super().marry()
