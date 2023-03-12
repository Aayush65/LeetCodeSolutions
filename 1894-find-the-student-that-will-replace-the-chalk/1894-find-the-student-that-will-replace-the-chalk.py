class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        if k == 0:
            return 0
        for i in range(len(chalk)):
            k -= chalk[i]
            if k < 0:
                return i