def LinkedListLoopDetection(node):
    fast = node
    slow = node
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if isSameNode(fast, slow):
            return True
    return False


