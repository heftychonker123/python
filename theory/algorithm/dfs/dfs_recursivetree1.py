
#dfs for a tree
def dfs(root,graph):
    print(root)
    if graph.get(root,[]):
        for i in graph.get(root,[]):
            dfs(i,graph)
    else:
        return
graph={
    "1": ["2", "3"],
    "2": ["5"],
    "3": ["4"],
    "4":[],
    "5":[],
}
dfs("1",graph)