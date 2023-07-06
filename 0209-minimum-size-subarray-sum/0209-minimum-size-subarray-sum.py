class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        minLen = len(nums) + 1
        total = 0
        while i < len(nums):
            if j < len(nums):
                while j < len(nums) and total < target:
                    total += nums[j]
                    j += 1
            else:
                break
            while i <= j and total >= target:
                minLen = min(minLen, j - i) 
                total -= nums[i]
                i += 1

        return 0 if minLen == len(nums) + 1 else minLen