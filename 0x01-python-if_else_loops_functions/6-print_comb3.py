#!/usr/bin/python3

for i in range(0, 90):
    f = i / 10
    s = i % 10

    if f < s:
        if i != 89:
            print("{:02d}".format(i), end=", ")
        else:
            print("{:02d}".format(i))
