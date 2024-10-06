f= None 
try:
    f= open('abc.txt','r')

except:
    print('Some Problem while locating and opeaning the file')

else:
    print('File Opened Sucessfully ')
    print('This data present in the file is :')
    print('*'*50)
    print(f.read())

finally: #Cleanup Activity
    if f is not None:
     f.close()