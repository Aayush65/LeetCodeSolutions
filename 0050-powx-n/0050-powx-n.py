class Solution:
    def myPow(self, x: float, n: int) -> float:
        isNegative = n / abs(n) if n else 1
        res = 1
        if n == 1:
            return x
        if n == 0:
            return res
        n = abs(n)
        if n % 2:
            half = self.myPow(x, n // 2)
            res = half * half * x
        elif n:
            half = self.myPow(x, n // 2)
            res = half * half
        return res if isNegative == 1 else 1 / res
