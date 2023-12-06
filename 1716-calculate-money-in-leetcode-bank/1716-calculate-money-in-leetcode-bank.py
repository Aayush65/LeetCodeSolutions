class Solution:
    def totalMoney(self, n: int) -> int:
        # 2 * (1 + ... + 7) + 7 x 1 + 7 X 2 + 7 x 3
        weeks = n // 7
        total = weeks * 28 + 7 * weeks * (weeks - 1) // 2
        n %= 7
        total += n * (n + 1) // 2 + n * weeks
        return total