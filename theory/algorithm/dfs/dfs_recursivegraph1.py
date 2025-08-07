def dfs_recursive(root, graphs, goal, path=None, allpath=None):
    if path is None:
        path = []
    if allpath is None:
        allpath = []

    path.append(root)

    if root == goal:
        allpath.append(path.copy())  # Save a copy of the successful path
    else:
        for neighbor in graphs.get(root, []):
            if neighbor not in path:
                dfs_recursive(neighbor, graphs, goal, path, allpath)

    path.pop()  # Backtrack to explore other paths
    return allpath


graphs = {
    "1": ["2", "3","5"],
    "2": ["5"],
    "3": ["4"],
    "4":["5"],
    "5":[],
}

print(dfs_recursive("1", graphs,"5"))
