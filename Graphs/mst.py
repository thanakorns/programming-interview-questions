from pythonds.graphs import PriorityQueue, Graph, Vertex

def prim(G,start):
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        pq.insert(v)
    start.setDistance(0)
    pq.insert(start)
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for v in currentVert.getConnections():
            newCost = currentVert.getWeight(v)
            if v.getDistance() < newCost:
                v.setDistance(newCost)
                v.setPred(currentVert)
                pq.decreaseKey(v, newCost)



