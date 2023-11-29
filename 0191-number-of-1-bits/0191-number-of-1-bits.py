class Solution:
    @cache
    def hammingWeight(self, n: int) -> int:
        return self.hammingWeight(n // 2) + (n & 1) if n else 0