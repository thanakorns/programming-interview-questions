def listOfDepth(node):
    return helper(node, 0, hashMap)

def helper(node, level, hashMap):
    if node == None
        return None
    if len(hashMap[level]) == 0:
        hashMap[level] = []
    hashMap[level].append(node)
    helper(node.left, level+1, hashMap)
    helper(node.right, level+1, hashMap)
    return node

def listOfDepthBFS(node):
    queue = []
    queue.push(node)
    node.visited = True
    node.level = 0
    hashMap[""+node.level] = node
    while len(queue) != 0:
        popped = queue.pop(0)
        for n in popped.neighbors:
            queue.push(n)
            n.visited = True
            n.level = popped.level + 1
            if len(hashMap[""+n.level]) == 0:
                hashMap[""+n.level] = []
            hashMap[""+n.level].push(n)

def listOfDepth(node):
    queue = []
    queue.push(node)
    levelList = []
    currentList = []
    currentList.push(node)
    while len(currentList) > 0:
        levelList.push(currentList)
        parentList = currentList
        currentList = []
        for v in parentList:
            if v.left != None:
                currentList.push(v.left)
            if v.right != None:
                currentList.push(v.right)










