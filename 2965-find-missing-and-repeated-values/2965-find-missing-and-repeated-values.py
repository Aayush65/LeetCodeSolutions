class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hs = {i for i in range(1, n * n + 1)}
        res = []
        for i in grid:
            for j in i:
                if j not in hs:
                    res.append(j)
                else:
                    hs.remove(j)
        res.append(hs.pop())
        return res