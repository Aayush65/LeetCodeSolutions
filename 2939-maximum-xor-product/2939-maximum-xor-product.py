class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod = int(1e9 + 7)
        for i in range(n - 1, -1, -1):
            a, b = max(a, b), min(a, b)
            bit = 1 << i
            if a & b & bit:
                continue
            if not a & bit and not b & bit:
                a |= bit
                b |= bit
            elif a & bit and not b & bit:
                a ^= bit
                b ^= bit
        return (a * b) % mod