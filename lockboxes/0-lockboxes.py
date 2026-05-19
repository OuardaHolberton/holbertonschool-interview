#!/usr/bin/python3
"""Module for lockboxes problem."""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened.

    Args:
        boxes (list of list): Each box contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < n and key not in opened:
            opened.add(key)
            for new_key in boxes[key]:
                if new_key not in opened:
                    keys.add(new_key)

    return len(opened) == n
