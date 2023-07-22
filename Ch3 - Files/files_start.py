#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

def main():
    # Open a file for writing and create it if it doesn't exist
    f = open("file.txt", "w", newline='\r\n')

    # Open the file for appending text to the end
    # f = open("file.txt", "a+")

    # write some lines of data to the file
    # important to remember "%" operator that is used for string formatting
    # and passing the value to its related place in string %d<-(i+1)
    # every argument must come inside a () immediately after % operator, like below:
    for i in range(10):
        f.write("this line is %d %d\n" % ((i + 1), (i + 2)))

        # other ways to perform string formatting:
        # using str.format() method or f-strings (formatted string literals);

        # 1- Using the str.format() method,
        # you can create a string with placeholders enclosed in curly braces {},
        # then call the format() method on the string,
        # passing in the values to be substituted for the placeholders. For example:
        # i = 42
        # s = "this line is {}\r\n".format(i+1)
        # f.write(s)

        # 2- Alternatively, you can use f-strings,
        # which are available in Python 3.6 and later.
        # F-strings allow you to embed expressions inside string literals,
        # enclosed in curly braces {}.
        # The expressions are evaluated at runtime
        # and their values are inserted into the resulting string.
        # For example:
        # i = 42
        # s = f"this line is {i+1}\r\n"
        # f.write(s)

        # close the file when done
    f.close()

    # Open the file back up and read the contents

    f = open("file.txt", "r")

    if f.mode == "r":
        # check to make sure that the file was opened
        # use the read() function to read the entire file
        # contents = f.read()
        # print (contents)
        fl = f.readlines()
        # readlines() reads the individual lines into a list
        for x in fl:
            print(x)


if __name__ == "__main__":
    main()
