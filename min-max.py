def minimax(depth, nodeIndex, isMax, values, height):
    if depth == height:
        return values[nodeIndex]
    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        ) 
values = [2, 3, 5, 9, 0, 1, 7, 5]
import math
height = int(math.log2(len(values)))
optimal_value = minimax(0, 0, True, values, height)
print("Optimal value:", optimal_value)
