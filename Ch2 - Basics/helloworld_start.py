#
# Example file for HelloWorld
# LinkedIn Learning Python course by Joe Marini
#

def main():
    print("Hello World")
    name = input("What is your name?")
    print("Nice to meet you ", name)

# python does not look for a specific function when the program starts
# checking to see that this module, file of python code, is
# loaded and the interpreter has assigned the __name__ variable, the value of main
# that means this python program was executed as a main program
# it was started from the command line or invoked from the python executable somehow
# and therefore this function right here, the main function should be called.
# now, the reason I needed to do this is that python code can be used multiple ways.
# My code in this file can be run as its own program, but I could also build a reusable module
# that can be included inside other python programs.
# So if I were using this code in another program,
# I wouldn't want all this code to just start running when it was imported into the other program,
# because that would cause problems.
# so lines _ and _ help distinguish between when a python file is being included in another program,
# or when that python code is being executed as its own program.
# So in this case, the file is being executed as a program and this, if condition right here, will evaluate to true,
# and then the main function will be called.
#


if __name__ == "__main__":
    main()
