from collections import deque

def dfs_all_paths_to_leaves(root, graph):
    stack = deque([(root, [root])])  # Each item is (node, current path)
    all_paths = []

    while stack:
        node, path = stack.pop()
        children = graph.get(node, [])
        if not children:  # Leaf node
            all_paths.append(path)
        else:
            for neighbor in reversed(children):  # Reversed for correct DFS order
                stack.append((neighbor, path + [neighbor]))  # Create a new path
    return all_paths

graph={
    "1":["2","3","4"],
    "2":["5"],
    "3":["6","7"],
    "4":[],
    "5":["8","9"],
    "6":[],
    "7":[],
    "8":[],
    "9":[],
}
print(dfs_all_paths_to_leaves("1",graph))