# x= 10.2           #integer
# y= 10         #float  
# z= "hello"      #string

# x=x*y

# print(type(x

#if we replace the x into y then

# y=x*y

# print(type(y))

#if we add any integer with any float number then it will be float, which means float is on proirity

# x=x+y                      #this process is called implicit type connversion
# print(x, "type of x is:", type(x))

#if we subtract then 

# x=x-y
# print(x, "type of x is:", type(x))

#if we want to multiply then:

# x=x*y
# print(x, "type of x is:", type(x))

#if we divide then we shall see the x type:

# x=x/y
# print(x, "type of x is:", type(x))


# explicit type conversion
from unicodedata import name


# age=input("whats your age? ")
# # age=int(age)
# print(age, type(int(age)))

#name
name=input("whats your name? ")
print(name, type(str(name)))