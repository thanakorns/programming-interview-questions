def sortstack(stack1):
    stack2 = Stack()
    while len(stack1) != 0:
        popped = stack1.pop()
        if len(stack2) == 0:
            stack2.push(popped)
        while popped < stack2.peek():
            stack1.push(stack2.pop())
        stack2.push(popped)
    while len(stack2)  != 0:
        stack1.push(stack2.pop())
    return stack1




