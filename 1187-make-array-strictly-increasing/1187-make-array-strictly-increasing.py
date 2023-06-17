class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        
        @cache
        def dp(index: int, prev: int) -> int:
            if index == len(arr1): return 0
            
            res = float("inf")
            if arr1[index] > prev: 
                res = dp(index + 1, arr1[index])
            idx = bisect_left(arr2, prev + 1)
            if idx == len(arr2):
                return res
            res = min(res, 1 + dp(index + 1, arr2[idx]))
            return res
            
        
        res = dp(0, -1)
        return -1 if res == float("inf") else res