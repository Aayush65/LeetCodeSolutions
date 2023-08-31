class Solution:
    def minTaps(self, n, ranges):
        maxReach = [0] * (n + 1)
        
        for i in range(len(ranges)):
            s = max(0, i - ranges[i])
            e = i + ranges[i]
            maxReach[s] = e
        
        tap = 0
        currEnd = 0
        nextEnd = 0
        
        for i in range(n + 1):
            if i > nextEnd:
                return -1
            if i > currEnd:
                tap += 1
                currEnd = nextEnd
            nextEnd = max(nextEnd, maxReach[i])
        
        return tap
