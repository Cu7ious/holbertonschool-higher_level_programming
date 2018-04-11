#!/usr/bin/python3

for i in range(97, 123):
    if i is 101 or i is 113:
        continue
    else:
        print("{:s}".format(chr(i)), end="")
