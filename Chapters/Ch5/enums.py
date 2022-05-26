# define enumerations using the Enum base class


from enum import Enum, auto, unique


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 4
    PEAR = auto()


def main():
    # enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # print the auto-generated value
    print(Fruit.PEAR.value)

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "dummy text"
    print(myFruits[Fruit.BANANA])


if __name__ == "__main__":
    main()