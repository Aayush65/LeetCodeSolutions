class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:       
        while targetX % 2 == 0:
            targetX //= 2
        while targetY % 2 == 0:
            targetY //= 2
        return gcd(targetX, targetY) == 1
            