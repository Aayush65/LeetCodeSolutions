class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return (x1 - x2)**2 + (y1 - y2)**2
        sides = {tuple(p1), tuple(p2), tuple(p3), tuple(p4)}
        if len(sides) < 4:
            return False
        lengths = Counter([dist(p1, p2), dist(p1, p4), dist(p1, p3), dist(p2, p3), dist(p2, p4), dist(p3, p4)])
        return len(lengths) == 2 and lengths[min(lengths)] == 4 and lengths[max(lengths)] == 2