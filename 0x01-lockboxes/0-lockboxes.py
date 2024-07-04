#!/usr/bin/python3
""" lockbox module"""


def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked from box 0."""
    stack = [0]
    visited = [False for i in range(len(boxes))]
    visited[0] = True
    while stack:
        current_box = stack.pop()
        # Iterate through keys in the current box
        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)
    return False not in visited
