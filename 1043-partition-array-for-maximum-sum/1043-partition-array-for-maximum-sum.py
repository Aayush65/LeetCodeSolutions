class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        @cache
        def dp(index: int) -> int:
            if index == len(arr):
                return 0
            res = 0
            currMax = 0
            for i in range(k):
                if i + index == len(arr):
                    break
                currMax = max(currMax, arr[index + i])
                res = max(res, currMax * (i + 1) + dp(index + i + 1))
            return res
    
        
        return dp(0)