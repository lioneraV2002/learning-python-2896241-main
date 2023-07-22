#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    while (x < 5):
        print(x)
        x += 1

    # TODO: define a for loop
    for (x) in range(5, 12):
        print(x)

    # TODO: use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for (y) in days:
        print(y)

    # TODO: use the break and continue statements
    z = 0
    for (z) in range(0, 20):
        if z % 3 == 0:
            continue
        else:
            print(z)

    for z in range(0, 10):
        if z == 6:
            break
        else:
            print(z)

    # ***************************************************************
    # TODO: using the enumerate() function to get index
    for i, d in enumerate(days):
        print(i, d)
    # ***************************************************************

if __name__ == "__main__":
    main()
