class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = int(1e9 + 7)
        stack = []
        res = 0
        for i, x in enumerate(arr):
            dels = 0
            while stack and stack[-1][0] > x:
                amt, cnt, idx = stack.pop()
                dels += cnt
                res += amt * cnt * (i - idx)
                res %= mod
            stack.append([x, dels + 1, i])

        while stack:
            amt, cnt, idx = stack.pop()
            res += amt * cnt * (len(arr) - idx)
            res %= mod
        return res