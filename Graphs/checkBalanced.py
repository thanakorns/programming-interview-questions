def checkBalanced(node):
    if node == None:
        return 0
    height_left = checkBalanced(node.left)
    height_right = checkBalanced(node.right)
    diff = abs(height_left - height_right)
    if height_left == -1 or height_right == -1 or diff > 1:
        return -1
    else:
        return diff + 1
