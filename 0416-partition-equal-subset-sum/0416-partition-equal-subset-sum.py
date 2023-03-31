class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        if numSum % 2:
            return False
        
        @cache
        def choice(index: int, target: int) -> bool:
            if target < 0:
                return False
            if not target:
                return True
            if index == len(nums):
                return False
            res = choice(index + 1, target - nums[index]) or choice(index + 1, target)
            return res
        
        return choice(0, numSum // 2)