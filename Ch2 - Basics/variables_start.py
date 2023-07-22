# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers ( integers and floating point values ), Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one": 1, "two": 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works (redeclare variables types works)
myint = "abc"
print(myint)

# to access a member of a sequence type, use [], they are zero-based index
print(mylist[2])
print(mytuple[1])

# use slices to get parts of a sequence ( access subset of a sequence )
# for example, the code below shows a subset of the list from mylist[1] to mylist[4]
# or rather, from the second column of the list to the fifth column
print(mylist[1:5])

# a third optional perimeter, called a step value, in other words, it is how many items to skip over
# for example getting subset of list from ( start index ) place of the list
# to the ( end index - 1 ) place of the list while skipping every second one
print(mylist[1:5:2])

# you can use slices to reverse a sequence
# for example, in the code below I didn't specify the start and end value,
# which by default means I want the entire list and -1 to reverse the direction of the steps
# instead of going forward, it traverses back
print(mylist[::-1])

# dictionaries are accessed via keys, and return the value of the associated key
# the keys are unique but the values need not
print(mydict["one"])

# ERROR: variables of different types cannot be combined
print("String type" + 123)

# the correct way of concatenation in this case, the built-in function str()
print("String type" + str(123))


# Global vs. local variables in functions
# when you are inside a function definition,
# the function its own local copy of whatever variables you declare inside the function
# if I actually want to affect the mystr variable, i should tell the function that the global value is my target
def someFunction():
    mystr = "def"
    print(mystr)


someFunction()
print(mystr)


def someOtherFunction():
    global mystr
    mystr = "def111"
    print(mystr)


someOtherFunction()
print(mystr)

# you can delete variables in real time using the "del" statement
del mystr
# if we print it, we will get a NameError
print(mystr)
