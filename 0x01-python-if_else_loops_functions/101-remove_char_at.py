#!/usr/bin/python3


def remove_char_at(str, n):
    """Returns the copy of the string 'srt'
    without the character at the position n"""

    count = 0
    result = ""

    while len(str) != count:
        if count != n:
            result += str[count]

        count += 1

    return result
