class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        isKey = lambda x: 'a' <= x <= 'f'
        isLock = lambda x: 'A' <= x <= 'F'
        isValid = lambda i, j: -1 < i < m and -1 < j < n and grid[i][j] != '#'

        keys = [0] * 6
        start = []
        for i in range(m):
            for j in range(n):
                if isKey(grid[i][j]):
                    keys[ord(grid[i][j]) - ord('a')] = 1
                if grid[i][j] == '@':
                    start = [i, j]
        keys = sum(2 ** i for i in range(6) if keys[i])

        q = {(start[0], start[1], 0)}
        visited = set()
        steps = 0
        while q:
            newQ = set()
            for i, j, k in q:
                if (i, j, k) in visited or not isValid(i, j):
                    continue
                if isValid(i, j) and isKey(grid[i][j]):
                    k |= 2 ** (ord(grid[i][j]) - ord('a'))
                visited.add((i, j, k))
                if k == keys:
                    return steps
                if isLock(grid[i][j]) and k & 2 ** (ord(grid[i][j]) - ord('A')) == 0:
                    continue

                newQ.add((i + 1, j, k))
                newQ.add((i, j + 1, k))
                newQ.add((i - 1, j, k))
                newQ.add((i, j - 1, k))

            q = newQ
            steps += 1
        return -1