#Nesting
try:
    print('Outer try block')
    try:
        print('Inner try block')

    except ValueError: 
        print('Inner except block')
    
    finally:
        print('Inner Finally block')

except:
    print('Outer except block')

finally:
    print('Outer finally block')
    