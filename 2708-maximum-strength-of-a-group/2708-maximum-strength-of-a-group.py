class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        ans = 0
        def dp(index: int, score: int) -> None:
            if index == len(nums):
                if score:
                    nonlocal ans
                    ans = max(ans, score)
                return
            dp(index + 1, score)
            dp(index + 1, score * nums[index] if score else nums[index])

        dp(0, None)
        return ans