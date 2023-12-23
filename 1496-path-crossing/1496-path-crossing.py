class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        curr = (0, 0)
        directionMap = {'N': (0, 1), 'S': (0, -1), 'E': (-1, 0), 'W': (1, 0)}
        for i in path:
            curr = (curr[0] + directionMap[i][0], curr[1] + directionMap[i][1])
            if curr in visited:
                return True
            visited.add(curr)
        return False