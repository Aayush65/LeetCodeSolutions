class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        ops = n
        indexMap = {nums[i]: i for i in range(len(nums))}
        nums.sort()
        for i in range(1, n):
            if indexMap[nums[i]] < indexMap[nums[i - 1]]:
                ops += n - i
        return ops