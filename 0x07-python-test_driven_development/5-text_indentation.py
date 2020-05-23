#!/usr/bin/python3
"""
Prints a text with 2 new lines after each coincidence
Characters: . ? and :
Return: Mone
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each coincidence
    Characters: . ? and :
    Return: None"""

    if isinstance(text, str):
        tkn = ['.', '?', ':']
        jump = 0
        for mv, x in enumerate(text):
            if x in tkn:
                print(text[jump:mv + 1].strip() + "\n")
                jump = mv + 1
        print(text[jump:].strip(), end='')
    if not isinstance(text, str):
        raise TypeError('text must be a string')
