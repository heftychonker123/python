from collections import deque
import math
#dfs to count the longest sequence to a leaf node
#i am too lazy to do dp with a data structure

def dfs(root, graph):
    stack = deque([(root, [root])])  # Each item is (node, current path)
    max_length=0

    while stack:
        node, path = stack.pop()
        children = graph.get(node, [])
        if not children:  # Leaf node
            max_length=max(max_length,len(path))
        else:
            for neighbor in reversed(children):  # Reversed for correct DFS order
                stack.append((neighbor, path + [neighbor]))  # Create a new path
    return max_length
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of relationships of influence
graph = {}

for i in range(n):
    x, y = map(int, input().split())
    
    if x not in graph:
        graph[x] = []
    if y not in graph:
        graph[y] = []
        
    graph[x].append(y)
t=0
for l in graph:
    t=max(t,(dfs(l,graph)))
print(t)

