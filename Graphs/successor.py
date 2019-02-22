def successor(node):
    result = None
    if node != None:
        if isLeftChild(node):
            result = left_helper(node)
        else:
            result = right_helper(node)
    return result

def left_helper(node):
    if node.right == None:
        return node.parent
    else:
        current = node.right
        while current.left != None:
            current = current.left
        return current

def right_helper(node):
    if node.right == None:
        parent = node.parent
        while(parent != None and parent.right == node):
            node = parent
            parent = parent.parent
        return parent
    else:
        current = node.right
        while current.left != None:
            current = current.left
        return current

def isLeftChild(node):
    parent = node.parent
    if parent.left == node:
        return True
    return False
