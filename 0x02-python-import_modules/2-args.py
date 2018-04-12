#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    l = len(argv) - 1
    count = 0
    args = "{:d} argument"

    args = args if l == 1 else args + "s"
    args = args + "." if l == 0 else args + ":"

    print(args.format(l))

    for arg in argv:
        if count:
            print("{:d}: {:s}".format(count, arg))
        count += 1
