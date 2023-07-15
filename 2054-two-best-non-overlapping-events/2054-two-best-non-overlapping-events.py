class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        
        maxList = []
        currMax = 0
        for i in range(n - 1, -1, -1):
            currMax = max(currMax, events[i][2])
            maxList.append(currMax)
        maxList.reverse()
        
        maxScore = 0
        for i in range(n):
            score = events[i][2]
            nextStartIdx = bisect_left(events, events[i][1] + 1, key = lambda x: x[0])
            if nextStartIdx < n:
                nextBest = maxList[nextStartIdx]
                score += nextBest
            maxScore = max(maxScore, score)
        return maxScore