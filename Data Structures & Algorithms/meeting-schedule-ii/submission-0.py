"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        first = 1000000
        last = -1
        for interval in intervals:
            first = min(first, interval.start)
            last = max(last, interval.end)
        map = {}
        for i in range(last-first):
            map[first+i] = 0
        for interval in intervals:
            for i in range(interval.end-interval.start):
                map[interval.start+i] += 1
        ret = 0 
        for key, val in map.items():
            ret = max(ret, val)
        return ret
        

