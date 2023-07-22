#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x is equal to y"
    else:
        result = "x is greater than y"

    print(result)

    # conditional statements let you use "a if C else b"

    result = "x is less than y" if x < y else "x is greater or equal to y"
    print(result)

    # match-case makes it easy to compare multiple values
    value = "threes"
    match value:
        case "one":
            result = "one"
        case "two":
            result = "two"
        case "three" | "four":
            result = (3, 4)

        # default case
        case _:
            result = -1

    print(result)


if __name__ == "__main__":
    main()
