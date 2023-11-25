def reconstruct_path(came_from: dict, start_id: int, end_id: int) -> list[""]:
    points = ['A', 'B', 'C', 'D', 'E', 'F']
    curr_id = end_id
    if curr_id not in came_from:
        return []

    path = []
    while curr_id != start_id:
        path.append(points[curr_id])
        curr_id = came_from[curr_id]

    path.append(points[start_id])
    path.reverse()
    return path