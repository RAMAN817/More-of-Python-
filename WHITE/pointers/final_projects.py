#Program to generate fake employee data for database testing
from random import *
alphabets= 'abcdefghijklmnopqrstuvwxyxz'
digits= '0123456789'
cities= ['Hyderbad','Chennai','Bangalore','Pune','Delhi','Mumbai']
designations= ['Software Engineer','Senior Software Engineer','Team Lead','Project Lead',
'Project Manager']
#To genrerate fake name
def get_fake_name():
  name =choice(alphabets).upper()
  n =randint(2,9)
  for i in range(n):
    name= name+choice(alphabets)
  return name

#To generate fake salary
def get_fake_digits():
  eno= 'e-'
  for i in range(4):
   eno= eno+choice(digits)
  return eno


#To generate fake salary
def get_fake_salary():
  esal= uniform(10000,50000)
  return esal


def get_fake_city():
    city= choice(cities)
    return city


#To generate fake mobile number
def get_fake_mobile():
  mobileno= choice('6789')
  for i in range(9):
    mobileno= mobileno+choice(digits)
  return mobileno

#To get fake designation
def get_fake_designation():
  designation=choice(designations)
  return  designation

#To generate fake employee data
def get_fake_emp_data():
  print(get_fake_name())
  print(get_fake_mobile())
  print(get_fake_salary())
  print(get_fake_digits())
  print(get_fake_designation())
  print(get_fake_city())

get_fake_emp_data()

