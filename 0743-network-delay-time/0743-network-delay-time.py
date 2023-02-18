class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodeMap = {i + 1: [] for i in range(n)}
        for i, j, t in times:
            nodeMap[i].append([j, t])

        timeMap = {i + 1: float("inf") for i in range(n)}
        timeMap[k] = 0
        h = [[0, k]]
        while h:
            time, poped = heappop(h)
            for i, t in nodeMap[poped]:
                if timeMap[i] > time + t:
                    heappush(h, [time + t, i])
                    timeMap[i] = time + t
        
        maxTime = 0
        for i in timeMap:
            if timeMap[i] == float("inf"):
                return -1
            maxTime = max(maxTime, timeMap[i])
        return maxTime