from collections import deque

graph = {
    1:[2,3],
    2:[1],
    3:[1]
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

bfs(graph, 1)

