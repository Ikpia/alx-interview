#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    ''' it calculate the fewest number of operation that is needed to result in exactly n H
    characters in this file
    Returns: Integer : if n is not possible to achieve, return 0
    '''
    pasted_chars = 1  # how many chars are in the file
    clipboard = 0  # how many H's are copied
    counter = 0  # counter

    while pasted_chars < n:
        # if it did not copy anything yet
        if clipboard == 0:
            # copy all
            clipboard = pasted_chars
            # increment the operations counter
            counter += 1

        # if you haven't pasted anything yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # increment the operations counter
            counter += 1
            # continue to next the loop
            continue

        remaining = n - pasted_chars  # remaining chararacters to Paste
        # check if not possible by checking if clipboard has more than what is needed to reach the number that's desire
        # which also means number of characters in the file is equal or more than in the clipboard. in both situations it's not possible to achieve number of characters
        if remaining < clipboard:
            return 0

        # if cannot be devided
        if remaining % pasted_chars != 0:
            # paste the current clipboard
            pasted_chars += clipboard
            # increment the operations counter
            counter += 1
        else:
            # copy all
            clipboard = pasted_chars
            # paste
            pasted_chars += clipboard
            # incrementthe  operations counter
            counter += 2

    # if desired result is gotten
    if pasted_chars == n:
        return counter
    else:
        return 0
