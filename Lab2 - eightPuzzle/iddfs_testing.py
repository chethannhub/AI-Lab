def dls(node, target, depth, tree, visited):
    if depth < 0:
        return False
    visited.append(node)
    if node == target:
        return True
    if node not in tree:
        return False
    for child in tree[node]:
        if dls(child, target, depth - 1, tree, visited):
            return True
    return False

def iddfs(root, target, max_depth, tree):
    for depth in range(max_depth + 1):
        visited = []  
        print(f"Depth {depth}: {visited}")
        if dls(root, target, depth, tree, visited):
            print(f"Path found at depth {depth}: {visited}")
            break
        else:
            print(f"No path found at depth {depth}")
    return visited

tree = {
    'a': ['b', 'c'],
    'b': ['d', 'e'],
    'c': ['f', 'g'],
    'd': ['h'],
    'f': ['i']
}

trace = iddfs('a', 'g', 4, tree)

print(f"\nTraversal path to 'g': {trace}")
