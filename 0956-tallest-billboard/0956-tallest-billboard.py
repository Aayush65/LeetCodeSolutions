class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        @cache
        def dp(index: int, diff: int) -> int:
            if index == len(rods):
                return -float("inf") if diff else 0
            res = dp(index + 1, diff + rods[index]) + rods[index]
            res = max(res, dp(index + 1, diff - rods[index]), dp(index + 1, diff))
            return res
        
        return dp(0, 0)
