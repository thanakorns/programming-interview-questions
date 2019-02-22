def firstcommonancestor(node, targetNode1, targetNode2, fca):
    if node == null:
        return fca

    if node == targetNode1 or node == targetNode2:
        return fca

    left_inorder = inorder(node.left, targetNode1, targetNode2, fca)

    right_inorder = inorder(node.right, targetNode1, targetNode2, fca)

    if (left_inorder == 'found two'):
        fca = node.left
        fca = firstCommonAncestor(node.left, targetNode1, targetNode2, fca)

    if (right_inorder == 'found two'):
        fca = node.right
        fca = firstCommonAncestor(node.right, targetNode1, targetNode2, fca)

    if (left_inorder == 'found one') and (right_inorder == 'found one'):
        fca = node

    return fca

def firstcommonancestor(root, p, q):
    if root == None or root == p or root == q:
        return root

    pOnLeft = covers(root.left, p)
    qOnLeft = covers(root.left, q)
    if pOnLeft != qOnLeft:
        return root
    branchNode = root.left if pOnLeft else root.right
    return firstcommonancestor(branchNode, p, q)

def covers(root, p):
    if root == None:
        return False
    if root == p:
        return True
    return covers(root.left, p) || covers(root.right, p)

def firstcommonancestor(root, p, q):
    if root == None:
        return None
    if root == p or root == q:
        return root
    left = firstcommonancestor(root.left, p, q)
    right = firstcommonancestor(root.right, p, q)

    if left != None and right != None:
        return root
    if left == None and right == None:
        return None
    return left if left != None else right



