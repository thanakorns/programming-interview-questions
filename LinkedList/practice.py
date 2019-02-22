class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head != None:
            while current.next != None:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


def bubblesort(array):
    for i in range(len(array)-1, -1, -1):
        for j in range(1, i):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
    return array


sortedarray = bubblesort([4, 5, 6, 1, 20, 21])
print(sortedarray)



