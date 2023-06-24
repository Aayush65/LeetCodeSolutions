class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        
        h = [[sum(mat[i][0] for i in range(m)), [0] * m]]
        visited = set()
        for i in range(k - 1):
            oldSum, coords = heappop(h)
            coords = list(coords)
            for i in range(m):
                if coords[i] == n - 1:
                    continue
                currSum = oldSum - mat[i][coords[i]] + mat[i][coords[i] + 1]
                coords[i] += 1
                if tuple(coords) not in visited:
                    heappush(h, (currSum, tuple(coords)))
                visited.add(tuple(coords))
                coords[i] -= 1
        return heappop(h)[0]