class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        i = 0
        count = 0
        while i < len(intervals):
            j = i + 1
            while j < len(intervals) and intervals[j][0] < intervals[i][1]:
                j += 1
                count += 1
            i = j
        return count