class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def isIncr(arr: list[int]) -> bool:
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False
            return True
        
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if isIncr(nums[:i] + nums[j + 1:]):
                    count += 1
        return count