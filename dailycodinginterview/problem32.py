from math import log

def findArbitrage(currencyTable):
    graph = []
    for i in range(len(currencyTable)):
        graph.append([])
        for j in range(len(currencyTable[i])):
            graph[i].append(-log(currencyTable[i][j]))

    src = 0
    n = len(graph)
    min_dist = [float('inf')] * n

    min_dist[src] = 0

    for i in range(n-1):
        for v in range(len(graph)):
            for w in range(len(graph[v])):
                if min_dist[w] + graph[v][w] < min_dist[v]:
                    min_dist[v] = min_dist[w] + graph[v][w]

    for v in range(len(graph)):
        for w in range(len(graph[v])):
            if min_dist[w] + graph[v][w] < min_dist[v]:
                return True
    return False
