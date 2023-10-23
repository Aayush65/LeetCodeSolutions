class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        maxIdx = nums.index(max(nums))
        minIdx = nums.index(min(nums))        
        
        a, b = min(maxIdx, minIdx), max(maxIdx, minIdx)
        n = len(nums)
        
        opposite = a + 1 + n - b
        left = b + 1
        right = n - a        
        
        return min(opposite, left, right)