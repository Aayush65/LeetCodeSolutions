class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        msb = int(log2(n))
        return 2 ** (msb + 1) - 1 - self.minimumOneBitOperations(n ^ (1 << msb))