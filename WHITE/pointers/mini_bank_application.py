class Customer:
    '''This class Developed by Roman and describe bank operation'''
    bankname= 'GLOBAL IME BANK'
    def __init__(self,name,balance=0.0) -> None:
        self.name= name
        self.balance= balance
    
    def deposit(self,amount):
        self.balance= self.balance + amount
        print('After deposit your balance:',self.balance)
    
    def withdraw(self,amount):
        if amount > self.balance:
            print('Insufficient Balance...')

        else:
            self.balance=self.balance - amount
            print('You have withdraw{}and now your balance is {}'.format(amount,self.balance))

print('Welcome to',Customer.bankname)
name= input('Enter your name')
c= Customer(name)
while True:
    print('d-deposit\nw-withdraw\ne-Exit')
    option=input('Choose your option:')
    if option.lower()== 'd':
        amount= float(input('Enter the amount to deposit:'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input('Enter amount to withdraw:'))
        c.withdraw(amount)
    elif option.lower()== 'e':
        print('Thanks for Banking')
        break
    
    else:
        print('Your option is Invalid ...please choose valid option')
