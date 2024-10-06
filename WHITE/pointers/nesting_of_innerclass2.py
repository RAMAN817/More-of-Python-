#Automation of calling another function after you call one
class Human:
    def __init__(self,name):
        self.name=name
        self.head=self.Head()
    
    def info(self):
        print('Hello, my name is',self.name)
        print('I am full busy with')
        self.head.talk()
        self.head.brain.think()
         
    class Head:
        def __init__(self):
            self.brain= self.Brain()

        def talk(self):
            print('Talking')

    
        class Brain:
            def think(self):
                print('Thinking')
human= Human('Roman')
human.info()
