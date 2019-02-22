class myqueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def pop(self):
        if len(self.stack1) == 0:
            while len(self.stack2) != 0:
                self.stack1.push(self.stack2.pop())
        return self.stack1.pop()

    def push(self, item):
        self.stack2.append(item)

    def peek(self):
        if len(self.stack1) == 0:
            while len(self.stack2) != 0:
                self.stack1.push(self.stack2.pop())
        return self.stack1.peek()


