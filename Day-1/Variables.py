# we can declare variable without any python in-built command
# let's try 

x=3
y=" Abdul saeed"
print(x)
print(y)

# variable can not be declared with specila data type but it can be changed after assigning value 

x= 23 #now it is int data type
z= 'ahmad' #now it is string data type 
print(x,z)


# Type casting 

# if you want to give special data type to variable then we can give by casting method 

a=int(2)  #2
b=str('ali')  #ali
c=float(3) #3.0
print(a,b,c) 


# getting the type of variables 

a=23
b='umer usama'
print(type(a))  # int class
print(type(b))   #str class


# case-senstivity

a=15
A=23
print(A,a)     # A will not overwrite the small "a"


#Variables name 

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

myName="saeed"
 
MYNAME= "saeed"

# camel case

myName="saeed"

# pascal case 

MYName="saeed"

# Snake case 

my_name="saeed"



#out-put variable 
x=4
name='ahmad'
#print(x+name) it will show an error  because int and str data type can not be concat so we use commas
print(x,name)

# global and local variables 

# global variable 
# a varibale that can be use everywhere either inside of function and also outer side of function 
# x= "global variable "
def myfunc():
  global x
  x="inside variable"
  print("this is " + x)
myfunc()
print(x)



