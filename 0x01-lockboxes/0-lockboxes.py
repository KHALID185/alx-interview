#!/usr/bin/python3
"""
This is a script provides a function for determining if all
boxes in a given list can be opened
"""


def canUnlockAll(boxes):
    unlocked = set([0])
    keys = boxes[0]

    while keys:
        new_key = keys.pop()
        if new_key < len(boxes) and new_key not in unlocked:
            unlocked.add(new_key)
            keys.extend(boxes[new_key])

    return len(unlocked) == len(boxes)
