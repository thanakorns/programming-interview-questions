def segregate(colorlist):
    rcount = 0
    gcount = 0
    for c in colorlist:
        if c == 'R':
            rcount += 1
        if c == 'G':
            gcount += 1
    rindex = 0
    gindex = rcount
    for i in range(len(colorlist)):
        if rindex == rcount:
            break
        if colorlist[i] == 'R':
            colorlist[i] = colorlist[rindex]
            colorlist[rindex] = 'R'
            rindex += 1
    for i in range(len(colorlist)):
        if gindex == rcount+gcount:
            break
        if colorlist[i] == 'G':
            colorlist[i] = colorlist[gindex]
            colorlist[gindex] = 'G'
            gindex += 1
    return colorlist

print(segregate(['G', 'B', 'R', 'R', 'B', 'R', 'G']))





