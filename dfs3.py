def dfs(graph, node, visited):
    print(node, end=" ")
    visited.add(node)
    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited) 
graph = {
    1: [2, 7],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [8, 10],
    8: [9],
    9: [],
    10: []
}
print("The DFS Traversal is:")
dfs(graph, 1, set())
