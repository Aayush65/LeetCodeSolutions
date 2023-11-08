class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx, sy) == (fx, fy):
            return t != 1
        if sx == fx:
            return abs(fy - sy) <= t
        if sy == fy:
            return abs(fx - sx) <= t
        return max(abs(fx - sx), abs(fy - sy)) <= t
