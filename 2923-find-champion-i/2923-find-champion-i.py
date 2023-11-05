class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        winner = [True] * n
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    winner[j] = False
        for i in range(n):
            if winner[i]:
                return i