BFS (Breadth-First Search) – Pseudocode:
BFS(Graph, startNode):
    create an empty Queue Q
    mark startNode as visited
    enqueue startNode into Q
    while Q is not empty:
        currentNode ← dequeue Q
        print currentNode
        for each adjacentNode of currentNode:
            if adjacentNode is not visited:
                mark adjacentNode as visited
                enqueue adjacentNode into Q

DFS:
DFS (Depth-First Search) – Pseudocode:
DFS(Graph, startNode):
    mark startNode as visited
    print startNode

    for each adjacentNode of startNode:
        if adjacentNode is not visited:
            DFS(Graph, adjacentNode)

MIN-MAX:
MINIMAX(node, depth, isMax)

    if depth = 0 or node is terminal
        return value of node

    if isMax = TRUE
        best ← -∞
        for each child of node
            val ← MINIMAX(child, depth-1, FALSE)
            best ← max(best, val)
        return best

    else
        best ← +∞
        for each child of node
            val ← MINIMAX(child, depth-1, TRUE)
            best ← min(best, val)
        return best
 
ALPHA-BETA PRUNING:
ALPHABETA(node, depth, α, β, isMax)

    if depth = 0 or node is terminal
        return value of node

    if isMax = TRUE
        best ← -∞
        for each child of node
            val ← ALPHABETA(child, depth-1, α, β, FALSE)
            best ← max(best, val)
            α ← max(α, best)
            if β ≤ α
                break   // PRUNE
        return best

    else
        best ← +∞
        for each child of node
            val ← ALPHABETA(child, depth-1, α, β, TRUE)
            best ← min(best, val)
            β ← min(β, best)
            if β ≤ α
                break   // PRUNE
        return best

