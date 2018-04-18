#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character."""
    char = sentence[0] if sentence else None
    return (len(sentence), char)
