class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        newQ = sorted(queries)
        
        n = len(intervals)
        ansMap = {}
        h = []
        i = 0
        for q in newQ:
            while i < n and intervals[i][0] <= q:
                size = intervals[i][1] - intervals[i][0] + 1
                heappush(h, (size, intervals[i][1]))
                i += 1
            while h and h[0][1] < q:
                heappop(h)
            if h:
                ansMap[q] = h[0][0]
            else:
                ansMap[q] = -1
        
        ans = []
        for q in queries:
            ans.append(ansMap[q])
        return ans