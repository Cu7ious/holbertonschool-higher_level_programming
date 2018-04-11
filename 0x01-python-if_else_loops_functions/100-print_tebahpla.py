#!/usr/bin/python3

for i in reversed(range(97, 123)):
    count = 1

    if i % 2 is not 0:
        i = chr(i - 32)
    else:
        i = chr(i)

    count = count + 1
    print("{:s}".format(i), end="")
