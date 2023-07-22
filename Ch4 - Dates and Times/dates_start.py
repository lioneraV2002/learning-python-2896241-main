#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#

from datetime import date
from datetime import datetime


def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today = date.today()
    print("today's date is: " + str(today))

    # TODO: print out the date's individual components
    print("date components: %02d - %02d - %04d" % (today.day, today.month, today.year))

    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    print("today's weekday: %d" % today.weekday())
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    print("which is: " + days[today.weekday()])

    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today = datetime.now()
    print("the current date and time is: " + str(today))

    # TODO: Get the current time
    t = datetime.time(datetime.now())
    print("current time is " + str(t))


if __name__ == "__main__":
    main()
