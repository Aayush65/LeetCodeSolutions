class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals) + 1
        intervals.sort(key = lambda x: [x[0], -x[1]])
        
        latest = intervals[0]
        for x, y in intervals:
            if y <= latest[1]:
                n -= 1
            else:
                latest = [x, y]
        return n