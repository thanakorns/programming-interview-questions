def sumLists(l1, l2):
    carry = 0
    sumNode = None
    while l1 != None or l2 != None:
        sum = carry
        if l1 != None:
            sum += l1.val
        if l2 != None:
            sum += l2.val
        digit = sum
        carry = 0
        if sum > 10:
            digit = sum - 10
            carry = 1
        if sumNode == None:
            sumNode = Node(digit)
        else:
            sumNode.next = Node(digit)
            sumNode = sumNode.next
        l1 = l1.next
        l2 = l2.next

def sumListsRecursive(l1, l2, carry):
    if (l1 == None and l2 == None and carry == 0):
        return None
    value = carry
    if l1 != None:
        value += l1.val
    if l2 != None:
        value += l2.val

    node = Node(value % 10)
    if (l1 != None or l2 != None or value >= 10):
        nextNode = sumListsRecursive(l1.next if l1 != None else None, l2.next if l2 != None else None, 1 if value >= 10 else 0)
        node = Node(value-10)
        node.next = nextNode
    return node









