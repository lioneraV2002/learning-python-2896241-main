#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
# def keyword + name + ( parameters ) + :
# the ":" indicates we are starting the body of the function
# all the statements should be indented equally so that they are obviously from the function body
# the number of indents can be set by me
def func():
    print("I am a function")


# TODO: function that takes arguments

def func2(arg1, arg2):
    print(arg1 + " " + arg2)


# TODO: function that returns a value
def cube(x):
    return x * x * x


# TODO: function with default value for an argument
# deefault value x = 1 in case it is not called
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num

    return result


# TODO: function that takes variable number of arguments
# using * character
# and the variable argument parameter always has to be last in defining parameters
# so that the interpreter knows which parameter is the variable arguments parameter
# multi_add (arg1, *args):

def multi_add(*args):
    result = 0
    for x in args:
        result += x

    return result


# calling the function directly
func()
# calling the function inside a print, it prints a string and then returns None ( since it has no return values )
# there will be two lines on the terminal when it is called
print(func())
# the function is not executed, we are only printing the value of the function definition itself,
# it means that functions themselves are objects that can be passed around and are values
print(func)
# ##################################
func2(12, 123)
print(func2(12, 123))
# ##################################
print(cube(3))
# ##################################
print(power(2))
print(power(2, 3))

# reversing the order in which the parameters are called
# the python interpreter figures out which arguments to supply the values to,
# when passing the values along with their names
print(power(x=2, num=3))
# ##################################
print(multi_add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
