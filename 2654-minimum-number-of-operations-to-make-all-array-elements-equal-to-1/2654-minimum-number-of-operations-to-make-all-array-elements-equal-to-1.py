class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i == 1:
                count += 1
        if count:
            return len(nums) - count
        
        res = float("inf")
        for i in range(len(nums)):
            hcf = nums[i]
            for j in range(i + 1, len(nums)):
                hcf = gcd(hcf, nums[j])
                if hcf == 1:
                    res = min(res, len(nums) + j - i - 1)
        return -1 if res == float("inf") else res