def dls_trace_path(tree, node, goal, depth, path, trace):
    path.append(node)
    trace.append(node)
    if depth == 0:
        if node == goal:
            return path.copy()
        path.pop()
        return None
    if depth > 0:
        for child in tree.get(node, []):
            result = dls_trace_path(tree, child, goal, depth - 1, path, trace)
            if result:
                return result
    path.pop()
    return None

def iddfs_trace_all(tree, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\n Searching at depth: {depth}")
        path = []
        trace = []
        result = dls_trace_path(tree, start, goal, depth, path, trace)
        print("Visited nodes:", trace)
        if result:
            print(f" Found goal '{goal}' at depth {depth}")
            print("Path to goal:", result)
            return result
    print(f"\n Goal '{goal}' not found within depth {max_depth}")
    return None

# Example tree
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
}

# Run the traced IDDFS
iddfs_trace_all(tree, 'A', 'G', 3)
