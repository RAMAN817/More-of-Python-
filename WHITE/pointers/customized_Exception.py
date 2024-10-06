class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg= msg

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg= msg

age= int(input('Enter Age:'))
if age>60:
   raise  TooYoungException('Please wait some more years pension is waiting for you')

elif age<18:
   raise TooOldException('Common man Lets grow your bead first')

else:
    print('Welcome to the tinder sir')