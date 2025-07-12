from collections import deque
from collections import deque

def dfs(root, graph):
    visited = set()
    stack = deque([root])
    
    while stack:
        v = stack.pop()  # Call the pop method with parentheses
        if v not in visited:
            print(v)  # Print after confirming it's unvisited
            visited.add(v)
            for neighbor in range (len(graph.get(v, []))-1,-1,-1):
                stack.append((graph.get(v,[]))[neighbor])  # Use append, not push

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
dfs("1",graph)