def deepest(node):
    if node and not node.left and not node.right:
        return (node, 1)

    if node.left and not node.right:
        return increment_depth(deepest(node.left))

    if node.right and not node.left:
        return increment_depth(deepest(node.right))

    result = max(deepest(node.left), deepest(node.right), key=lambda t: t[1])
    return increment_depth(result)


def increment_depth(node_depth_tuple):
    node, depth = node_depth_tuple
    return (node, depth + 1)

