# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2, *, SuppressExceptions=False):
    pass


def main():
    # can be called only with the keyword
    myFunction(1, 2, SuppressExceptions=True)


if __name__ == "__main__":
    main()
