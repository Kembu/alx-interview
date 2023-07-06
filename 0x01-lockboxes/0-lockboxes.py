uar/bin/env python3


def can_open_all_boxes(lockboxes):
    """
    Determines if all the boxes can be opened.

    Args:
        lockboxes: A list of lists representing the lockboxes and their keys.

    Returns:
        True if all boxes can be opened, False otherwise.
    """
    keys = [0]  # Start with the first box as the initial key
    for key in keys:
        for box in lockboxes[key]:
            if box not in keys and box < len(lockboxes):
                keys.append(box)
    if len(keys) == len(lockboxes):
        return True
    return False
