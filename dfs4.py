def dfs(graph, node, visited=set()):
    print(node, end=" ")
    visited.add(node)
    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited) 
graph = {
    1: [2,3],
    2: [5,6],
    3: [4,7],
    4: [8],
    5: [],
    6: [],
    7: [],
    8: []
}
print("dfs traversal")
dfs(graph, 1)
