# Strings in python are surrounded by either single quotation marks, or double quotation marks

print ("hello word")
print ('hello name')



# assigning a variable to string 

a= 'name'
print (a)

# multi line strings 

x=  """hey user  
     welcome to use string of multiline 
    with useful way
    """

print(x)


# looping through string 
str= "saeed"
for x in  str:
    print( x)  # s a e e d
    
    
# string lenght 

print (len (str))  #5


# checking string 

str2='hey buddy welcome to this course'
print("buddy" in str2)   # true
print("hello " in str2)    #false   

# is Not 

print ("hello " not in str2)  #true 