# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "This is a string"
    print(s)

    # Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    s1 = b.decode('utf-8')
    print(s + s1)

    b1 = s.encode('utf-8')
    print(b + b1)

    # encode the string as UTF-32
    b2 = s.encode('utf-32')
    print(b2)


if __name__ == "__main__":
    main()
