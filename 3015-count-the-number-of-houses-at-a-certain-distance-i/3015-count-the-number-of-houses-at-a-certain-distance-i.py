class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        res = [0] * n
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist1 = abs(i - j)
                dist2 = abs(i - x) + abs(y - j) + 1
                dist3 = abs(i - y) + abs(x - j) + 1
                dist = min(dist1, dist2, dist3)
                if 0 < dist < n:
                    res[dist - 1] += 1
        return res