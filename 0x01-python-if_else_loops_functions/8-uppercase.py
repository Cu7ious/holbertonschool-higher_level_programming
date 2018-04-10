def uppercase(str):
    """Prints a given string in uppercase."""

    string = ""

    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            string += chr(ord(c) - 32)
        else:
            string += c

    print(string)
