values = [2, 3, 5, 9, 0, 1, 7, 5]

# MAX at leaf pairs
pair_max = [
    max(values[0], values[1]),
    max(values[2], values[3]),
    max(values[4], values[5]),
    max(values[6], values[7])
]

# MIN level
left_min  = min(pair_max[0], pair_max[1])
right_min = min(pair_max[2], pair_max[3])

# MAX at root
result = max(left_min, right_min)

print("Output:", result)
