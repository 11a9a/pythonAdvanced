# Demonstrate the usage of Counter objects

from collections import Counter


def main():
    # list of students in class 1
    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah",
              "Kevin", "James", "James", "Melanie", "Penny", "Steve"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    # Create a Counter for each class
    ctr1 = Counter(class1)
    ctr2 = Counter(class2)

    # How many students in class 1 named James?
    print(f"{ctr1['James']} students with name James")

    # How many students are in class 1?
    print(f"{sum(ctr1.values())} students in class 1.")

    # Combine the two classes
    ctr1.update(class2)
    print(f"{sum(ctr1.values())} students in combined classes.")

    # What's the most common name in the two classes?
    print(
        f"{ctr1.most_common(1)[0][0]} is most common name by number {ctr1.most_common(1)[0][1]}.")

    # Separate the classes again
    ctr1.subtract(class2)

    # What's common between the two classes?
    print(ctr1 & ctr2)


if __name__ == "__main__":
    main()
