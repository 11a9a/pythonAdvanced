# use transform functions like sorted, filter, map


from curses.ascii import isupper


def filterOdds(x):
    return False if (x % 2 == 0) else True


def filterLower(x):
    return False if isupper(x) else True


def squareFunc(x):
    return (x**2)


def toGrade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    return 'F'


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74, 52)

    # use filter to remove items from a list
    odds = list(filter(filterOdds, nums))
    print(f"{odds=}")

    # use filter on non-numeric sequence
    lowers = list(filter(filterLower, chars))
    print(f"{lowers=}")

    # use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print(f"{squares=}")

    # use sorted and map to change numbers to grades
    letter_grades = list(map(toGrade, grades))
    print(f"{letter_grades=}")


if __name__ == "__main__":
    main()
