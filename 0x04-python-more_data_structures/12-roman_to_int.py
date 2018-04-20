#!/usr/bin/python3


def get_char_val(string, idx):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if (idx < 0):
        return 0

    return roman[string[idx]]


def roman_to_int(roman_string):
    """Converts a Roman number to an integer."""

    if (roman_string and isinstance(roman_string, str) is True):
        result = 0
        next_c = curr_c = 0
        index = len(roman_string) - 1

        while(index >= 0):
            c = index

            curr_c = get_char_val(roman_string, c)
            next_c = get_char_val(roman_string, c - 1)

            result += curr_c

            if next_c < curr_c:
                result -= next_c

                if index - 1 is 0:
                    break

            index -= 1

        return result
    else:
        return 0
