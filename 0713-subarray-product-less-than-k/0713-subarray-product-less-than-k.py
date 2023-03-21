class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k in {0, 1}:
            return 0
        j = 0
        currProd = 1
        total = 0
        for i in range(len(nums)):
            currProd *= nums[i]
            while currProd >= k:
                currProd //= nums[j]
                j += 1
            total += i - j + 1
        return total
            