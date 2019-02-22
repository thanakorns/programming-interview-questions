class SetofStacks:

    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = []

    def push(self, item):
        index = len(self.stacks) - 1
        if len(self.stacks) == 0:
            self.stacks.append([item])
        elif len(self.stacks[index]) >= self.threshold:
            newStack = []
            newStack.append(item)
            self.stacks.append(newStack)
        else:
            self.stacks[index].append(item)

    def pop(self):
        index = len(self.stacks) - 1
        value = self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            self.stacks.pop()
        return value


