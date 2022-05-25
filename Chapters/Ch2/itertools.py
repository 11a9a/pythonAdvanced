# advanced iteration functions in the itertools package

import itertools


def testFunction(x):
    return x < 40


def main():
    # cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1), next(cycle1), next(cycle1), next(cycle1))

    # use count to create a simple counter
    counter = itertools.count(0, 50)
    print(next(counter), next(counter), next(counter), next(counter))

    # accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30, 60, 30]
    acc = itertools.accumulate(vals, max)
    print(list(acc))

    # use chain to connect sequences together
    chn = itertools.chain("ABCD", [11, 2, 4, 5])
    print(list(chn))

    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))


if __name__ == "__main__":
    main()
