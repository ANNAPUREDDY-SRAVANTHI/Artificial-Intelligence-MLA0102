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

DECISION TREE

Algorithm DecisionTree(Dataset, Attributes, Target)

1. If all records in Dataset belong to the same Target class
      Return a Leaf node with that class

2. If Attributes list is empty
      Return a Leaf node with the majority Target class in Dataset

3. Select the Best_Attribute from Attributes
      (using Information Gain / Gini Index)

4. Create a Decision Node using Best_Attribute

5. For each value v of Best_Attribute:
      a. Create a subset Dataset_v where Best_Attribute = v

      b. If Dataset_v is empty
            Attach a Leaf node with majority Target class
         Else
            Attach subtree:
            DecisionTree(Dataset_v, Attributes − Best_Attribute, Target)

6. Return the Decision Node


WATER JUG PROBLEM
Algorithm WaterJugProblem(Jug1, Jug2, Target):

1. Start with both jugs empty: (0, 0)

2. Repeat until target is reached in any jug:
     a. Fill any jug completely
     b. Empty any jug completely
     c. Pour water from one jug to the other
        until one is full or the other is empty

3. Keep track of steps to reach the target

4. Stop when target is measured


