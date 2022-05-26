# Demonstrate the usage of namdtuple objects

import collections


def main():
    # create a Point namedtuple
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(15, 20)
    print(p1, p1.x)

    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)


if __name__ == "__main__":
    main()
