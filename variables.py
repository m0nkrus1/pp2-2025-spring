x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


#Variables Names
#Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Unpacking a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#Outputting a variable
x = "Python is awesome"
print(x)
#Outputting multiple variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#Adding value of the other variables
x = 5
y = 10
print(x + y)
#when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
print(x + y)
#Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x) # the result will be 'Python is awesome'

myfunc()



y = 'Wonderful'

def Function():
    y = "Excellent"  
    print("Python is", y)  
Function()  

print("Python is", y)  

def Myfunc():
    global z  
    z = "Amazing"  
    print('Python is', z)  
Myfunc()  

print("Python is", z)  


t = "Incredible"

def funct():
    global t  
    t = 'amazing'  

funct() 

print("Python is", t)  
