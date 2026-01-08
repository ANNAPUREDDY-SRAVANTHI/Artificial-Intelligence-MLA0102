def dfs(graph, node, visited=set()):
    print(node, end=" ")
    visited.add(node)

    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited) 
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
print(" The DFS Traversal is")
dfs(graph,'A')
