# customize string representations of objects


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return f"#{self.red:02x}{self.green:02x}{self.blue:02x}"
        else:
            raise AttributeError

    # use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # use dir to list the available properties
    def __dir__(self):
        return ("rgbcolor", "hexcolor")


def main():
    # create an instance of myColor
    color = myColor()
    # print the value of a computed attribute
    print(color.rgbcolor)
    print(color.hexcolor)

    # set the value of a computed attribute
    color.rgbcolor = (125, 200, 96)
    print(color.rgbcolor)

    # access a regular attribute
    print(color.red)

    # list the available attributes
    print(dir(color))


if __name__ == "__main__":
    main()
