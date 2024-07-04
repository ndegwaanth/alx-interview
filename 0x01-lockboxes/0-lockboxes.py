#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.
    arg:
        boxes: This are box to be checked.
    """
    n = len(boxes)  # Number of boxes
    opened = [False] * n  # Track which boxes have been opened
    opened[0] = True  # The first box is always open
    stack = [0]  # Start with the first box
    visited = set()  # To keep track of visited boxes

    while stack:
        current_box = stack.pop()
        if current_box in visited:
            continue
        visited.add(current_box)

        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
