def removeDups(head):
    current = head
    while current != None:
        checker = current
        while checker.next != None:
            if checker.next.val == current.val:
                checker.next = checker.next.next
            else:
                checker = checker.next
        current = current.next
    return head

def removeDupsHashMap(head):
    if head == None:
        return head
    hashTable = {}
    current = head
    hashTable[current.val] = 1
    while current.next != None:
        if current.next.val in hashTable:
            current.next = current.next.next
        else:
            current = current.next
            hashTable[current.val] = 1
    return head


