# class scheduling problem
import operator
from heapq import heappop, heappush

def minMeetingRooms(intervals):
    timelist = []
    for i in intervals:
        timelist.append(("start", i.start))
        timelist.append(("end", i.end))
    timelist.sort(key=operator.itemgetter(1, 0))
    numMeetingRoomsOn = 0
    ans = 0
    print(timelist)
    for time in timelist:
        if time[0] == "start":
            numMeetingRoomsOn += 1
        else:
            numMeetingRoomsOn -= 1
        ans = max(ans, numMeetingRoomsOn)
    return ans


def minMeetingRoomsMinHeap(intervals):
    heap = []
    intervals.sort(key=lambda x: x.start)
    for time in intervals:
        if heap and time.start >= heap[0]:
            heappop(heap)
        heappush(heap, time.end)
    return len(heap)

