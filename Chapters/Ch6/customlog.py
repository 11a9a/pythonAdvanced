# Demonstrate how to customize logging output

import logging

extData = {'user': 'johndoe@example.com'}


# add another function to log from
def dumbFunc():
    logging.debug("This is a debug-level log message", extra=extData)


def main():
    # set the output file and debug level, and
    # use a custom formatting specification
    formatstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
    formatdate = "%d/%m/%Y %I:%M:%S %p"
    logging.basicConfig(filename="customout.log",
                        level=logging.DEBUG,
                        format=formatstr,
                        datefmt=formatdate)

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    dumbFunc()


if __name__ == "__main__":
    main()
