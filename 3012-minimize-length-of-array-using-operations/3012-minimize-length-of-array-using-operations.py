class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        mini = min(nums)        
        for i in nums:
            if i % mini:
                return 1
        return ceil(nums.count(mini) / 2)