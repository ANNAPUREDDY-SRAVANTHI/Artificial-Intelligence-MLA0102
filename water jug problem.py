from collections import deque
def water_jug_bfs(jug1, jug2, target):
    # Initial state (jug1, jug2)
    start = (0, 0)
    visited = set()
    queue = deque()
    queue.append((start, []))  

    while queue:
        (a, b), path = queue.popleft() 
        if a == target or b == target:
            print("Solution path:")
            for step in path + [(a, b)]:
                print(step)
            return True 
        if (a, b) in visited:
            continue
        visited.add((a, b)) 
        moves = [] 
        moves.append((jug1, b 
        moves.append((a, jug2)) 
        moves.append((0, b)) 
        moves.append((a, 0)) 
        pour = min(a, jug2 - b)
        moves.append((a - pour, b + pour)) 
        pour = min(b, jug1 - a)
        moves.append((a + pour, b - pour)) 
        for move in moves:
            if move not in visited:
                queue.append((move, path + [(a, b)]))

    print("No solution found.")
    return False

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

water_jug_bfs(jug1_capacity, jug2_capacity, target_amount)
