def findRouteBetweenNodes(src, target):
    queue = []
    queue.add(src)
    src.visited = True
    while not queue.isEmpty():
        current = queue.pop(0)
        if current == target:
            return True
        for n in current.neighbors:
            if n.visited == False:
                queue.push(n)
                n.visited = True
    return False

