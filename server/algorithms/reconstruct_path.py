def reconstruct_path(came_from: dict, start_id: int, end_id: int) -> list[int]:
    curr_id = end_id

    path = []
    if curr_id not in came_from:
        return []

    while curr_id != start_id:
        path.append(curr_id)
        curr_id, edge_id = came_from[curr_id]
    path.append(curr_id)
    path.reverse()


    return path