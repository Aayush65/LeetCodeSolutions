class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        def calcRhombusArea(r: int, c: int, rad: int):
            val = 0
            #left-top
            for i in range(rad):
                val += grid[r + i][c - i]
            #right-top
            for i in range(1, rad):
                val += grid[r + i][c + i]

            #left-bottom
            newR, newC = r + rad - 1, c - rad + 1
            for i in range(1, rad):
                val += grid[newR + i][newC + i]

            #right-bottom
            newR, newC = r + rad - 1, c + rad - 1
            for i in range(1, rad - 1):
                val += grid[newR + i][newC - i]

            return val

        h = set()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                for r in range(1, min(j + 1, n - j) + 1):
                    if i + 2 * r - 2 >= m:
                        break
                    h.add(calcRhombusArea(i, j, r))
                    if len(h) > 3:
                        h.remove(min(h))
        return sorted(list(h), reverse = True)