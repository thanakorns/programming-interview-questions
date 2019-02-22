class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashValue = self.hashFunction(key, len(self.slots))
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
        elif self.slots[hashValue] == key:
            self.data[hashValue] = data
        else:
            nextHashValue = self.rehash(hashValue, len(self.slots))
            while self.slots[nextHashValue] != None and self.slots[nextHashValue] != key:
                nextHashValue = self.rehash(nextHashValue, len(self.slots))

            if self.slots[nextHashValue] == None:
                self.slots[nextHashValue] = key
                self.data[nextHashValue] = data
            else:
                self.data[nextHashValue] = data

    def hashFunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def get(self, key):
        startSlot = self.hashFunction(key, len(self.slots))
        currentSlot = startSlot
        while self.slots[currentSlot] != None:
            if self.slots[currentSlot] != key:
                currentSlot = self.rehash(currentSlot, len(self.slots))
                if currentSlot == startSlot or self.slots[currentSlot] == None:
                    break
            elif self.slots[currentSlot] == key:
                return self.data[currentSlot]
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
