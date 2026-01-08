from collections import deque

# Adjacency list representation of the graph
graph = {
    1: [2, 3],
    2: [4,5],
    3:[],
    4: [],
    5: []
}

# Source node
start = 1

# BFS logic
visited = set([start])
queue = deque([start])

print("BFS Traversal:", end=" ")

while queue:
    node = queue.popleft()
    print(node, end=" ")
    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
