#Encapsulation = Data Hiding + Abstraction
class Account:
    def __init__(self,initial_balance):
        self.__balance= initial_balance

    def getBalance(self):
        #validiation | Authentication
        return self.__balance

    def   deposit(self,amount):
        #Validation| Authentication
        self.__balance = self.__balance+ amount
    
    def withdraw(self,amount):
        #Validation| Authentication
        self.__balance= self.__balance- amount

    # GuI = Abstraction 
    