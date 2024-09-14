# For comment single or multiple line we use "cltr+/" or '''comment'''.

# To get mutiple cursor we have to press "alt+lmb" to select multiple cursor.

# To move a line we have to press "alt+up/down arrow key".

# To duplicate lines we have to press "alt+shift+down arrow key".

# Escape sequence characters and parameters of print statement:
''' To add new line we use (\n) '''

from ast import Index

print("Arpit Rawat is a Good Boy.\nHe is very Great in Nature.")
''' To add single/double quotes we use (\' or \") '''
print("Arpit Rawat is a \"Good Boy\".He is very Great in Nature.")
''' To add Tab/space we use (\t) '''
print("\tArpit Rawat is a Good Boy.He is very Great in Nature.")
''' To add any character between words we use separator i.e (,sep= "any symbol/character or space")'''
print("Arpit Rawat is a Good Boy.He is very Great in Nature." , 1,2,3,4,sep= "-")
''' To add two line we use (end= " anything else ") '''
print("Arpit Rawat is a Good Boy.He is very Great in Nature.", end= " ")
print("Arpit Rawat is a Good Boy.He is very Great in Nature.")


# Variable: variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc. Creating a variable is like creating a place holder in memory and assigning it some value. In puthon its as easy as writing.
a = 1234567890
b = "Ram,Shyam,Mohan,Sita."
c = True
d = None
e = 1.2
print(a)
print(b)
'''Data Type:
# integer (int) = 1,2,3,4,5,6,7,8,9,0,etc.
#float = 1.1,1.2,2.3,4.5,etc
# boolean (bool) = True , False.
# String (str) = "anything except integers".
# None (NoneType) = None '''

# To find the type of any data type we write print(type())
print("The type of a is",type(a))
print("The type of b is",type(b))
print("The type of c is",type(c))
print("The type of d is",type(d))
print("The type of e is",type(e))



# Arithmetic operators
#  Operator	    Operator Name	     Example
#   +	           Addition	          15+7
#   -          	Subtraction	          15-7
#   *           Multiplication	      5*7
#   **	          Exponential	      5**3
#   /	            Division	      5/3
#   %	            Modulus	          15%7
#   //	         Floor Division	      15//7

print(5+6)
print(15-6)
print(15*6)
print(15/6)
print(15//6)
print(5%3)
print(2**5)
# Typecasting : The conversion of one data type to other data type is known as type casting in python or type conversion in python.Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.
x = "4"
y = "5"
print(int(x)+int(y))
#  Taking User Input in python :In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable.
p=input("Enter the name: ")
print('Hello '+p)
X = input("Enter first number: ")
Y = input("Enter second number: ")
print("The sum of two number is", int(X) + int(Y))


# What are strings?
# In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

# Multiline Strings
# If our string has multiple lines, we can create them like this:

A = """This is an Example of multiple line string
We can use triple double quotes or single quotes.
To print multiple lines in python."""
print(A)

# Accessing Characters of a String
'''In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.'''

 #The "11th" number of term "E" is printed in output.
print(A[11])

# Looping through the string
# We can loop through strings using a for loop like this:

for character in A :
    print(character)

# String Slicing & Operations on String
# Length of a String"
# We can find the length of a string using len() function.
    
names = "Arpit,Ram"
print("names contains", len(names) , "letter word")

# if else conditons

Budget = int(input("Enter Your Budget"))
appleprice = 150
if (Budget > appleprice):
    print("Arpit, Add 1Kg Apple to my Cart")
elif (Budget == 150):
    print("Arpit, Add 1/2Kg Apple to my Cart")
else:
    print("Arpit, Dont Add Apples to my Cart")


# for loop

colours = ["red", "green", "blue", "yellow", "orange", "pink", "black"]
for colour in colours:
    print(colour)
    for i in colour:
        print(i)

for k in range(1,1001,1):
    print(k)

print("Even numbers from 1 to 100")
for k in range(2, 102, 2,):
    print(k)


# while loop
i = int(input("Enter the number:"))
while(i<=30):
    i = int(input("Enter the number:"))
    print(i)
print("Done with the loop")




# function
def calculategmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
a = 97
b = 42
c = 10
d = 19
e = 18
f = 17
g = 19
h = 78
calculategmean(a,b)
calculategmean(c,d)
calculategmean(e,f)
calculategmean(g,h)

def function_name(parameters):
  pass

def name(fname, lname):
    print("Hello,", fname, lname)

name("Arpit", "Rawat")
print("Now See The Design/Pattern")



# Turtle Animation


import turtle
turtle.setup(width=600, height=500)
turtle.reset()
turtle.hideturtle()
turtle.speed(0)

turtle.bgcolor('black')

c = 0
x = 0


colors = [
#reddish colors
(1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
#orangey colors
(1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
#yellowy colors
(1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
#greenish colors
(0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
#blueish colors
(0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
]

while x < 1000:
    idx = int(c)
    color = colors[idx]
    turtle.color(color)
    turtle.forward(x)
    turtle.right(98)
    x = x + 1
    c = c + 0.1

turtle.exitonclick()


