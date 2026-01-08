from collections import deque 
graph = {
    1: [2,3],
    2: [4],
    3: [],
    4: [5],
    5: []
} 
start = 1
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
