def reconstruct_path(came_from: dict, start_id: int, end_id: int) -> list[int]:
    curr_id = end_id

    path = []
    if curr_id not in came_from:
        for key, value in came_from.items():
            if len(value) != 1:
                curr_id, edge_id = value
                path.append(edge_id)
    else:
        while curr_id != start_id:
            curr_id, edge_id = came_from[curr_id]
            path.append(edge_id)
        path.reverse()

    return path