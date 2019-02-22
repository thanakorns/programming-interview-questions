def findIntersection(l1, l2):
    current = l1
    l1_length = 0
    while current != None:
        l1_length += 1
        if current.next == None:
            tail1 = current
        current = current.next
    current = l2
    l2_length = 0
    while current != None:
        l2_length += 1
        if current.next == None:
            tail2 = current
        current = current.next
    if not isSameNode(tail1, tail2):
        return False
    head = l1 if l1_length > l2_length else l2
    head2 = l1 if l1_length <= l2.length else l2
    diff = abs(l1_length - l2_length)
    counter = 0
    while counter < diff:
        head = head.next
        counter += 1
    while head != None and head2 != None:
        if isSameNode(head, head2):
            return True
        head = head.next
        head2 = head2.next
    return False







