def partition(head, val):
    current = head
    secondListHead = None
    firstListTail = None
    firstListHead = None
    secondListTail = None
    while current != None:
        next = current.next
        if current.val <= val:
            if firstListTail == None:
                firstListTail = current
                firstListHead = current
            else:
                firstListTail.next = current
                firstListTail = firstListTail.next
        else:
            if secondListHead == None:
                secondListHead = current
                secondListTail = current
            else:
                temp = secondListHead
                secondListHead = current
                secondListHead.next = temp
        current = next
    firstListTail.next = secondListHead
    secondListTail.next = None
    return firstListHead


def partitionEfficient(node, val):
    head = node
    tail = node
    node = node.next
    while(node != None):
        next = node.next
        if node.val < val:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = tail.next
    tail.next = None
    return head

