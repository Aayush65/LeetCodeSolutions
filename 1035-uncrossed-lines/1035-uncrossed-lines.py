class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        
        memo = {}
        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if i == n1 or j == n2:
                return 0
            if nums1[i] == nums2[j]:
                return 1 + dp(i + 1, j + 1)
            res = max(dp(i, j + 1), dp(i + 1, j))
            memo[(i, j)] = res
            return res
        
        return dp(0, 0)