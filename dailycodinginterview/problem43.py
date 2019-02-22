# stack does not contain the actual max
# self.max_elem always holds the current max
# if new item is bigger that current max, push an even bigger item and update max to be the new item so when you pop
# , if the popped elem is bigger than max, then you know that max_elem should be returned and you have a way to set max to prev max

class stack:
    def __init__(self):
        self.stack = []
        self.max_elem = float('-inf')

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.max_elem = val
        else:
            if val > self.max_elem:
                self.stack.append(2*val + max_elem)
                self.max_elem = val
            else:
                self.stack.append(val)

    def pop(self):
        if self.stack[-1] > self.max_elem:
            removedVal = self.stack.pop()
            current_max_elem = self.max_elem
            previous_max_elem = removedVal - 2 * self.max_elem
            self.max_elem = previous_max_elem
            return current_max_elem
        else:
            return self.stack.pop()

    def max(self):
        return self.max_elem

