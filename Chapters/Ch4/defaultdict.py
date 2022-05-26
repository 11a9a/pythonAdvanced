# Demonstrate the usage of defaultdict objects
from collections import defaultdict


def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = defaultdict(int)
    fCounter = defaultdict(lambda: 100)

    # Count the elements in the list
    for fruit in fruits:
        fruitCounter[fruit] += 1
        fCounter[fruit] += 1

    # print the result
    for (k, v), (c, d) in zip(fruitCounter.items(), fCounter.items()):
        print(k + ": " + str(v))
        print(c + ": " + str(d))


if __name__ == "__main__":
    main()
