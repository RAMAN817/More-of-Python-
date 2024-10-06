#WAp to specify file name and data dynamically from the keyboard.
fname= input("Enter the file name:")
f= open(fname,'w')
while True:
    data= input('Enter Data to Write ')
    f.write(data+'\n')
    option= input('Do you still wanna add some more files[Yes /no]')
    if option.lower()== 'no':
        break

print('Your provided data written to the files succesfully')
f.close()