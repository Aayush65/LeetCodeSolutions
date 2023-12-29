class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        from sortedcontainers import SortedSet

        n = len(rains)
        res = [-1] * n
        lastRain = {}
        avail = SortedSet()
        for i, x in enumerate(rains):
            if x:
                if x in lastRain:
                    last = lastRain[x]
                    dryingDateIdx = avail.bisect_right(last)
                    if dryingDateIdx == len(avail):
                        return []
                    dryingDate = avail[dryingDateIdx]
                    avail.pop(dryingDateIdx)
                    res[dryingDate] = x
                lastRain[x] = i
            else:
                res[i] = 1
                avail.add(i)
        return res