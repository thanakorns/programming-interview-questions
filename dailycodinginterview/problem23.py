def minimumSteps(map, start, end):
    q = []
    visited = [False] * len(map)
    for i in range(len(map)):
        visited[i] = [False] * len(map[0])
    visited[start[0]][start[1]] = 0
    q.append(start)
    while q:
        pos = q.pop(0)
        if pos == end:
            return visited[pos[0]][pos[1]]
        neighbors = getneighbors(pos, visited, map)
        for n in neighbors:
            visited[n[0]][n[1]] = visited[pos[0]][pos[1]] + 1
            q.append(n)
    return None


def getneighbors(pos, visited, map):
    neighbors = []
    top = (pos[0] - 1, pos[1])
    left = (pos[0], pos[1] - 1)
    right = (pos[0], pos[1] + 1)
    bot = (pos[0] + 1, pos[1])

    if pos[0]-1 >= 0 and map[top[0]][top[1]] == 'f' and not visited[top[0]][top[1]]:
        neighbors.append(top)
    if pos[1]-1 >= 0 and map[left[0]][left[1]] == 'f' and not visited[left[0]][left[1]]:
        neighbors.append(left)
    if pos[1]+1 <= len(map[0])-1 and map[right[0]][right[1]] == 'f' and not visited[right[0]][right[1]]:
        neighbors.append(right)
    if pos[0]+1 <= len(map[0])-1 and map[bot[0]][bot[1]] == 'f' and not visited[bot[0]][bot[1]]:
        neighbors.append(bot)
    return neighbors


map = [['f', 'f', 'f', 'f'],
       ['t', 't', 'f', 't'],
       ['f', 'f', 'f', 'f'],
       ['f', 'f', 'f', 'f']]

start = (3,0)
end = (0,0)

print(minimumSteps(map, start, end))





