def reconstruct_path(came_from: dict, start_id: int, end_id: int) -> list[int]:
    curr_id = end_id
    if curr_id not in came_from:
        return []

    path = []
    while curr_id != start_id:
        curr_id, edge_id = came_from[curr_id]
        path.append(edge_id)

    path.reverse()
    return path