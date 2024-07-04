#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    This function determines if all the boxes can be opened
    arg:
        boxes : This are boxes to be checked.
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is always open
    keys = [0]  # Start with the first box

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)
    return all(opened)
