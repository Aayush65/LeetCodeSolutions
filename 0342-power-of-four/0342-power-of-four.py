class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and int(log(n, 4)) == log(n, 4)