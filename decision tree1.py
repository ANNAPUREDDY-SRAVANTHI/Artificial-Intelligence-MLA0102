import math
from collections import Counter 
data = [
    ['T','Hot','High','No'],
    ['T','Hot','High','No'],
    ['F','Hot','High','Yes'],
    ['F','Cool','Nor','Yes'],
    ['F','Cool','Nor','Yes'],
    ['T','Cool','High','No'],
    ['T','Hot','High','No'],
    ['T','Hot','Nor','Yes'],
    ['F','Cool','Nor','Yes'],
    ['F','Cool','High','Yes']
]

features = ['A1','A2','A3'] 
def entropy(data):
    labels = [row[-1] for row in data]
    total = len(labels)
    counts = Counter(labels)
    ent = 0
    for c in counts.values():
        p = c / total
        ent -= p * math.log2(p)
    return ent 
def info_gain(data, index):
    total_entropy = entropy(data)
    values = set(row[index] for row in data)
    weighted = 0
    for v in values:
        subset = [row for row in data if row[index] == v]
        weighted += (len(subset)/len(data)) * entropy(subset)
    return total_entropy - weighted 
def id3(data, features):
    labels = [row[-1] for row in data]
    if labels.count(labels[0]) == len(labels):
        return labels[0]

    if not features:
        return Counter(labels).most_common(1)[0][0]

    gains = [info_gain(data, i) for i in range(len(features))]
    best = gains.index(max(gains))
    tree = {features[best]: {}}

    values = set(row[best] for row in data)
    for v in values:
        subset = [row[:best] + row[best+1:] for row in data if row[best] == v]
        sub_features = features[:best] + features[best+1:]
        tree[features[best]][v] = id3(subset, sub_features)

    return tree 
def print_tree(tree, indent=""):
    if isinstance(tree, dict):
        for key in tree:
            print(indent + str(key))
            for value in tree[key]:
                print(indent + " └─" + str(value) + ":")
                print_tree(tree[key][value], indent + "   ")
    else:
        print(indent + " → " + tree) 
tree = id3(data, features)
print("\nDecision Tree:\n")
print_tree(tree)
