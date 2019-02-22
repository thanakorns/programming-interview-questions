class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def helper(root):
    if root is None:
        return (None,0)
    right_node, right_depth = helper(root.left)
    left_node, left_depth = helper(root.right)
    if left_node is None and right_node is None:
        return (root, 1)
    elif left_node is None:
        return (right_node, right_depth+1)
    elif right_node is None:
        return (left_node, left_depth+1)
    return (right_node, right_depth+1) if right_depth > left_depth else (left_node, left_depth+1)

def deepest_node(root):
    return helper(root)[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.right.left = TreeNode(6)

print(deepest_node(root).val)
print(deepest_node(root2).val)




'''

a

(e, 4)  (f, 5)
b     c
'''