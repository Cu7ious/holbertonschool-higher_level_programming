#!/usr/bin/python3


def roman_to_int(roman_string):
    """Converts a Roman number to an integer."""

    if (roman_string and isinstance(roman_string, str) is True):
        roman = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        prev = 0
        result = 0

        for c in roman_string:
            if prev < roman[c]:
                result -= prev * 2

            prev = roman[c]
            result += roman[c]

        return result
    else:
        return 0
