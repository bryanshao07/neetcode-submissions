"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #Sort interval by start time
        intervals.sort(key = lambda x : x.start)
        heap = []
        for interval in intervals:
            #if curr start is after most recent end meeting, we can reuse that room 
            if heap and interval.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        return len(heap)