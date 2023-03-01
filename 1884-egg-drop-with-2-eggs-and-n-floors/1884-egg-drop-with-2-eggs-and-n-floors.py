class Solution:
    def twoEggDrop(self, n: int) -> int:
        D = sqrt(1 + 8 * n)
        return ceil((D - 1) / 2)