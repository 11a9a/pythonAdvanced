# demonstrate template string functions


from string import Template


def main():
    # Usual string formatting with format()
    str1 = "I'm reading {0} by {1}".format("Martin Iden", "Jack London")
    print(str1)

    # create a template with placeholders
    template = Template("I'm reading ${title} by ${author}")

    # use the substitute method with keyword arguments
    str2 = template.substitute(title="Martin Iden", author="Jack London")
    print(str2)

    # use the substitute method with a dictionary
    data = {
        "title": "Martin Iden",
        "author": "Jack London"
    }
    str3 = template.substitute(data)
    print(str3)


if __name__ == "__main__":
    main()
