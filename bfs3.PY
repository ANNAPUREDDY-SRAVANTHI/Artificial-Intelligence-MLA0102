from collections import deque 
graph = {
    1: [2, 7],
    2: [3, 6],
    7: [8, 10],
    3: [4,5],
    6: [],
    8: [9],
    10: [],
    4: [],
    5: [],
    9: []
    
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
