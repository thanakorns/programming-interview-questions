class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, currentSize):
        index = currentSize
        while(index // 2 > 0):
            parentIndex = index // 2
            if self.heapList[index] < self.heapList[parentIndex]:
                self.swap(index, parentIndex)
            index = parentIndex

    def swap(self, index, parentIndex):
        temp = self.heapList[parentIndex]
        self.heapList[parentIndex] = self.heapList[index]
        self.heapList[index] = temp

    def delMin(self):
        min = self.heapList[1]
        self.swap(1, self.currentSize)
        self.heapList.pop()
        self.percDown(1)
        return min

    def percDown(self, i):
        while i * 2 <= self.currentSize:
            minChildIndex = self.minChildIndex(i)
            if self.heapList[minChildIndex] < self.heapList[i]:
                self.swap(i, minChildIndex)
            i = minChildIndex


    def minChildIndex(self, i):
        if( i*2 + 1 > self.currentSize):
            return i * 2
        else:
            return i*2 if self.heapList[i*2] < self.heapList[i*2+1] else i*2+1


    def buildHeap(self, arr):
        i = len(arr) // 2
        self.currentSize = len(arr)
        self.heapList = [0] + arr[:]
        while i > 0:
            self.percDown(i)
            i = i - 1




binHeap = BinHeap()
binHeap.buildHeap([4,2,8,3,2,9,10,3,5])
binHeap.insert(1)
print(binHeap.heapList)
binHeap.heapList = [2,3,4,5,65]
print(binHeap.heapList)
binHeap2 = BinHeap()