def flight_itin_helper(targetLength, s, e, flightlist, resultlist):
    if len(resultlist) == targetLength:
        return resultlist

    for i in range(len(flightlist)):
        flight = flightlist[i]
        resultlist.append(flight.start)
        resultlist.append(flight.end)
        flightlist.pop(i)
        if isValid(resultlist):
            return flight_itin_helper(targetLength, s, e, flightlist, resultlist)
        flightlist.insert(i, flight)
        resultlist.pop()
        result.list.pop()

    return None

def isValid(s, e, targetLength, resultlist):
    if len(resultlist) > 2:
        if resultlist[-2] == resultlist[-3]:
            return True
    elif len(resultlist) == targetLength:
        if resultlist[-1] == e:
            return True
    else:
        if resultlist[0] == s:
            return True
    return False

def flight_itinerary(flightlist, s, e):
    targetlength = len(flightlist) + 1
    resultlist = []
    resultlist = flight_itin_helper(targetlength, s, e, resultlist, flightlist)
    return resultlist
