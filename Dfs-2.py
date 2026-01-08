def dfs(graph, node, visited=set()):
    print(node, end=" ")
    visited.add(node)

    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited)

# Graph (Adjacency List)
graph = {
    1: [2, 3],
    2: [4,5],
    3:[],
    4: [],
    5: []
}
print(" The DFS Traversal is")
dfs(graph,1)
