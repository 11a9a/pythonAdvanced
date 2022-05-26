# Demonstrate the use of variable argument lists


# define a function that takes variable arguments
def addition(*args):
    res = 0
    for arg in args:
        res += arg
    return res


def main():
    # pass different arguments
    print(addition(1, 34, 23, 34))

    # pass an existing list
    l = [23, 23, 45, 12]
    print(addition(*l))


if __name__ == "__main__":
    main()
