#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if isinstance(a_dictionary, dict) is False:
        return None

    key = ""
    score = 0

    for k, v in a_dictionary.items():
        if score <= v:
            key = k
            score = v

    return key
