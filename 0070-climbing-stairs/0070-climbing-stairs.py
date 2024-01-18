class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1, 2]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n - 1]