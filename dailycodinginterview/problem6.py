class XORLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.both = None

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.both = 0x00 ^ get_pointer(self.tail)
        self.tail.both = 0x01 ^ get_pointer(self.head)
        self.size = 0

    def add(self, element):
        if self.head.both ^ 0x00 == get_pointer(self.tail):
            self.head.both = 0x00 ^ get_pointer(element)
        prevAddr = get_pointer(self.tail) ^ 0x01
        element.both = prevAddr ^ get_pointer(self.tail)
        self.tail.both = get_pointer(element) ^ 0x01
        self.size += 1


    def get(self, index):
        i = 0
        currentAddr = self.head.both ^ 0x00
        prevAddr = get_pointer(self.head)
        while i < index and i < self.size:
            oldCurAddr = currentAddr
            currentAddr = prevAddr ^ oldCurAddr
            prevAddr = oldCurAddr
            i += 1
        return dereference_pointer(current)

