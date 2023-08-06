class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        preSum = [0]
        for i in nums:
            preSum.append(preSum[-1] + i)
        n = len(nums)
        
        @cache
        def dp(lo: int, hi: int) -> bool:
            if lo == hi:
                return True
            res = False
            for i in range(lo, hi):
                if preSum[i + 1] - preSum[lo] < m and i - lo:
                    continue
                if preSum[hi + 1] - preSum[i + 1] < m and hi - i - 1:
                    continue
                res = res or (dp(lo, i) and dp(i + 1, hi))
            return res
            
        return dp(0, n - 1)