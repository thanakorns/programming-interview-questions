(0,1) (1, 1) (1, 0)

# brute force solution by creating a new board
class ConwayGameofLife:

    def __init__(self, livelist, ticks):
        self.livelist = livelist
        self.ticks = ticks

    def neighbors(self, pos):
        n = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 and j != 0:
                    n.append((pos[0]+i, pos[1]+j))
        return n

    def printBoard(self, livelist):


    def run(self):
        n = 0
        while n < self.ticks:
            relevantCells = []
            for pos in livelist:
                relevantCells.append(pos)
                n = neighbors(pos)
                relevantCells.append(n)
            for pos in relevantCells:
                newlivelist = []
                liveFriendsCount = 0
                n = neighbors(pos)
                # if current pos is alive
                if pos in livelist:
                    for each in n:
                        if each in livelist:
                            liveFriendsCount += 1
                    if liveFriendsCount == 2 or liveFriendsCount == 3:
                        newlivelist.append(pos)
                # if current pos is dead
                else:
                    for each in n:
                        if each in livelist:
                            liveFriendsCount += 1
                    if liveFriendsCount == 3:
                        newlivelist.append(pos)
            livelist = newlivelist
            printBoard(livelist)


