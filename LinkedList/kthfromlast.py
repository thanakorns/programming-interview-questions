def kthfromlast(head, k):
    p1 = head
    p2 = head
    for i in range(0, k):
        p2 = p2.next
        if p2 == None:
            return None
    while p2.next != None:
        p1 = p1.next
        p2 = p2.next
    return p1


def kthfromlastRecursive(node, k, counter):
    if node.next == None:
        counter = 1
        return node
    placeholderNode = kthfromlastRecursive(node.next, k, counter)
    counter += 1
    if counter == k:
        return node
    return placeholderNode


