def deleteMiddleNode(node):
    if node == None || node.next == None:
        return False
    node.val = node.next.val
    node.next = node.next.next
    return True

