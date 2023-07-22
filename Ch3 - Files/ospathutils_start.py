#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    print("item exists: " + str(path.exists("file.txt")))
    print("Item is a file: " + str(path.isfile("file.txt")))
    print("item is a directory: " + str(path.isdir("file.txt")))
    # Work with file paths
    print("item's real path: " + str(path.realpath("file.txt")))
    print("item's path and name: " + str(path.split(path.realpath("file.txt"))))

    # Get the modification time

    t = time.ctime(path.getmtime("file.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("file.txt")))

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("file.txt"))
    print("it has been " + str(td) + " since the file was modified")
    print("or, " + str(td.total_seconds()) + " seconds")


if __name__ == "__main__":
    main()
