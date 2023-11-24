class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        bob = len(piles) // 3
        total = 0
        for i in range(bob, len(piles), 2):
            total += piles[i]
        return total