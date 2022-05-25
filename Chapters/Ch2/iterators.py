# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # use iter to create an iterator over a collection
    i = iter(days)
    print(next(i), next(i), next(i))

    # iterate using a function and a sentinel
    with open("test.txt", "r") as file:
        for line in iter(file.readline, ''):
            print(line)

    # use regular iteration over the days
    for day in days:
        print(day)

    for i in range(len(days)):
        print(i+1, days[i])

    # using enumerate reduces code and provides a counter
    for i, day in enumerate(days, start=1):
        print(i, day)

    # use zip to combine sequences
    for day in zip(days, daysFr):
        print(day)

    # using zip and enumerate together
    for i, day in enumerate(zip(days, daysFr), start=1):
        print(
            f"Day {i} of a week in English is {day[0]} and {day[1]} in French.")


if __name__ == "__main__":
    main()
