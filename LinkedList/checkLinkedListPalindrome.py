def checkLinkedListPalindrome(node):
    if node == None or node.next == None:
        return True
    slow_runner = node
    fast_runner = node
    while (fast_runner.next != None):
        fast_runner = fast_runner.next
        if fast_runner.next != None:
            fast_runner = fast_runner.next
            stack.push(slow_runner)
            slow_runner = slow_runner.next
            s2 = slow_runner
        else:
            s2 = slow_runner.next

    while (not stack.isEmpty() and s2 != None):
        if stack.pop() != s2.val:
            return False
        s2 = s2.next
    return True


def checkLinkedListPalindrome(node):
    fast = node
    slow = node
    while fast != None and fast.next != None:
        stack.push(slow)
        slow = slow.next
        fast = fast.next.next

    if fast != None:
        slow = slow.next

    while slow != None:
        val = stack.pop()
        if val != slow.val:
            return False
        slow = slow.next
    return True


def checkLinkedListPalindromeReverseAndClone(node):
    reversed = reverseandclone(node)
    return isEqual(reversed, node)

def reverseandclone(node):
    head = None
    while node != None:
        newNode = LinkedListNode(node.val)
        newNode.next = head
        head = newNode
    return head


def isEqual(reversed, node):
    while reversed != None or node != None:
        if reversed.val != node.val or reversed == None or node == None:
            return False
        reversed = reversed.next
        node = node.next
    return True


def checklinkedListPalindromeRecursive(node, length):
    if node == None or length == 0:
        return Result(node, true)
    if length == 1:
        return Result(node.next, true)
    returned_result = checklinkedLisetPalindromeRecursive(node.next, length-2)

    if returned_result.result == False:
        return returned_result
    
    if node.val != returned_node.val:
        returned_result.result = False

    returned_result.node = node.next
    return returned_result













