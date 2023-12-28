class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        strMap = defaultdict(list)
        for i, j, val in zip(original, changed, cost):
            strMap[i].append((val, j))
        allLens = sorted(list({len(i) for i in original}))
        n = len(source)
        
        @cache
        def shortestDist(start: str, end: str) -> int:
            h = [(0, start)]
            visited = set()
            while h:
                cost, curr = heappop(h)
                if curr == end:
                    return cost
                if curr in visited:
                    continue
                visited.add(curr)
                for nextCost, nei in strMap[curr]:
                    heappush(h, (cost + nextCost, nei))
            return float("inf")
        
        @cache
        def dp(index: int) -> int:
            if index == n:
                return 0
            res = float("inf")
            if source[index] == target[index]:
                res = dp(index + 1)
            for i in allLens:
                if index + i > n:
                    break
                srcSubStr = source[index: index + i]
                trgSubStr = target[index: index + i]
                cost = shortestDist(srcSubStr, trgSubStr)
                if cost != float("inf"):
                    res = min(res, cost + dp(index + i))
            return res

        res = dp(0)
        return -1 if res == float("inf") else res