class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        one = nums.index(1)
        last = nums.index(len(nums))
        
        ops = one
        if one > last:
            last += 1
        ops += len(nums) - last - 1
        return ops