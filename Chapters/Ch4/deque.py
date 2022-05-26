# deque objects are like double-ended queues

import collections
import string


def main():
    # initialize a deque with lowercase letters
    letters = collections.deque(string.ascii_lowercase)
    print(letters)

    # deques support the len() function
    print(len(letters))

    # deques can be iterated over
    for letter in letters:
        print(letter.upper(), end=", ")

    # manipulate items from either end
    letters.pop()
    letters.popleft()
    letters.appendleft(1)
    letters.append(2)
    print(letters)

    # rotate the deque
    letters.rotate(10)
    print(letters)


if __name__ == "__main__":
    main()
