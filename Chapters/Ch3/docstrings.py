# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """Just prints arguments.

    Args:
        arg1 (any): first argument.
        arg2 (any, optional): second argument. Defaults to None.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
