class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd = 1 if high % 2 or low % 2 else 0
        return (high - low)//2 + odd