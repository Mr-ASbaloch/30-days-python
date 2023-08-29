# by using the slice method we can get range of character in python strings 
# we giv the starting index and the ending index in this way 
# but one thing always keep in mind that the start index value is included in new character but at te end one less is counted

a= 'hello world !'
print (a[2:5]) #llo
print(a[3:7])  #lo w


# slice from the start 
# when you leave out the first index character it always start by 0 index 

print(a[:4])  #hell

# slice to end 
# by leaving out the end index all range goes to end 

print(a[2:])  #llo world !


# negative indexing 

# we can give the negative index to range 

print (a[-5:-2])