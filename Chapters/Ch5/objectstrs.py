# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f"<Person Class - {self.fname=}, {self.lname=}, {self.age=}"

    # use str for a more human-readable string
    def __str__(self):
        return f"{self.fname} {self.lname} is {self.age}"

    # use bytes to convert the informal string to a bytes object
    def __bytes__(self):
        value = f"Person:{self.fname}:{self.lname}:{self.age}"
        return bytes(value.encode('utf-8'))


def main():
    # create a new Person object
    person = Person()

    # use different Python functions to convert it to a string
    print(repr(person))
    print(str(person))
    print("Formatted: {0}".format(person))
    print(bytes(person))


if __name__ == "__main__":
    main()
