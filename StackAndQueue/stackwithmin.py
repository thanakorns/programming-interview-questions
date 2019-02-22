class StackWithMin:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def is_empty(self):
        return self.stack == []

    def pop(self):
        value = self.stack.pop()
        if value == self.min():
            self.minStack.pop()
        return value

    def push(self, item):
        if item == self.min():
            self.minStack.append(item)
        self.stack.append(item)

    def min(self):
        return minStack[0] if len(minStack) != 0 else sys.max_size




