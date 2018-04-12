#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    c = 0
    result = 0

    for arg in argv:
        if c is not 0:
            result += int(arg)

        c += 1

    print("{}".format(result));
