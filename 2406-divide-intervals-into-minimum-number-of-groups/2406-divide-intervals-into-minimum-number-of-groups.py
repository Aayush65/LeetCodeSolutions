class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        i, j = 0, 0
        n = len(intervals)
        maxOverlap = 0
        overlap = 0
        while i < n:
            while i < n and start[i] <= end[j]:
                overlap += 1
                i += 1
            maxOverlap = max(maxOverlap, overlap)
            if i == n:
                break
            while j < n and end[j] < start[i]:
                overlap -= 1
                j += 1
        return maxOverlap