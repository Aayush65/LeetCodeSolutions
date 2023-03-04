class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minKPointer = maxKPointer = -1
        count = j = 0
        for i in range(len(nums)):
            if not minK <= nums[i] <= maxK:
                minKPointer = maxKPointer = -1
                j = i + 1
            else:
                if nums[i] == minK:
                    minKPointer = i
                if nums[i] == maxK:
                    maxKPointer = i
                count += max(0, min(maxKPointer, minKPointer) - j + 1)
        return count
