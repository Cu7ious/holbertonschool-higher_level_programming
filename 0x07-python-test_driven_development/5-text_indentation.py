#!/usr/bin/python3
"""
Text Indentation - the text_indentation program.
parses a `text` string for `.?:`, replaces it with the new line.
Prints: the parsed `text` string
"""


def text_indentation(text):
        """
        parses a `text` string for `.?:`, replaces it with the new line.
        """
        if not isinstance(text, str) or text is None:
            raise TypeError("text must be a string")

        if text == "":
            print()
            return

        text = text.replace(".", ".\n\n").replace("?", "?\n\n")
        text = text.replace(":", ":\n\n")

        print("\n".join(x.lstrip() for x in text.split("\n")), end="")
