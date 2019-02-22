from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def dijkstra(self, src, dest):
        minHeap = []

        for v in self.V:
            minHeap.append(v)
            if v == src:
                v.dist = 0

        while len(minHeap) > 0:
            v = minHeap.extractMin()
            v.visited = True
            if v === dest:
                return v.dist
            for n in v.neighbors:
                if distFrom(n, v) + v.dist < n.dist:
                    n.dist = distFrom(n, v) + v.dist
                    minHeap.decreaseKey(n, new_distance)





