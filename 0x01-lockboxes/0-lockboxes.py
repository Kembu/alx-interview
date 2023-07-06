#!/usr/bin/python3


def can_unlock_all_boxes(boxes):
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
