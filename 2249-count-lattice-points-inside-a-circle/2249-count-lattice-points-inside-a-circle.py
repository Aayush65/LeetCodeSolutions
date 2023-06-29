class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        dist = lambda x1, y1, x2, y2: (x1 - x2) ** 2 + (y1 - y2) ** 2
        
        allPoints = set()
        for x, y, r in circles:
            up, down = y + r, y - r
            left, right = x - r, x + r
            for i in range(left, right + 1):
                for j in range(down, up + 1):
                    if dist(i, j, x, y) <= r * r:
                        allPoints.add((i, j))
        return len(allPoints)