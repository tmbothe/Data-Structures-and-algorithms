import heapq
from typing import List

def minMeetingRooms(intervals: List[List[int]]) -> int:

    if not intervals:
        return 0
    free_rooms=[]
    intervals = sorted(intervals,key=lambda x :x[0])
    
    heapq.heappush(free_rooms, intervals[0][1])

    for i in intervals[1:]:
        print(free_rooms)
        if free_rooms[0]<=i[0]:
            heapq.heappop(free_rooms)
        heapq.heappush(free_rooms, i[1])
    print(f'final free rooms : {free_rooms}' )
    return len(free_rooms)




if __name__=='__main__':
    intervals = [[0,30],[5,10],[15,20]]
    print(minMeetingRooms(intervals))

    intervals = [[7,10],[2,4]]
    print(minMeetingRooms(intervals))
