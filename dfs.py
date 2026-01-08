def dfs(graph, node, visited=set()):
    print(node, end=" ")
    visited.add(node)
    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited) 
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [5],
    5: []
} 
dfs(graph, 1)
