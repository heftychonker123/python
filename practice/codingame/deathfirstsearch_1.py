from collections import deque
#bfs with start and end
def bfs_all_paths(graph, start, goal):
    queue = deque([[start]])  # queue stores paths, not just nodes
    all_paths = []

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            all_paths.append(path)
        else:
            for neighbor in graph[node]:
                if neighbor not in path:  # avoid cycles
                    new_path = path + [neighbor]
                    queue.append(new_path)

    return all_paths

n, l, e = [int(i) for i in input().split()]
graph={i:[] for i in range(n)}
g_arr=[]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    graph[n1].append(n2)
    graph[n2].append(n1)
for i in range(e):
    ei = int(input())  # the index of a gateway node
    g_arr.append(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    paths=[]
    for l in g_arr:
        paths+=bfs_all_paths(graph,si,l)
    max_length=10**9
    path_index=0
    for t in range(len(paths)):
        if len(paths[t])<max_length:
            max_length=len(paths[t])
            path_index=t
    print(*paths[path_index][-2:])
