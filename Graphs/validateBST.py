def validateBST(node):
    if node == None:
        return True
    if validateBST(node.left) and validateBST(node.right):
        if node.left != None and node.left.val > node.val:
            return False
        if node.right != None and node.right.val <= node.val:
            return False
        return True
    else:
        return False

last_printed = None
def validateBSTInorder(node):
    if node == None:
        return True
    if not validateBSTInorder(node.left):
        return False
    if last_printed != None and last_printed >= node.val:
        return False
    last_printed = node.val
    if not validateBSTInorder(node.right):
        return False
    return True

def validateBSTMinMax(node, min, max):
    if node == None:
        return True
    if (min != None and min > node) or (max != None and max <= node):
        return False
    if (not validateBSTMinMax(node.left, min, node.val) or not validateBSTMinMax(node.right, node.val, max)):
        return False
    return True


