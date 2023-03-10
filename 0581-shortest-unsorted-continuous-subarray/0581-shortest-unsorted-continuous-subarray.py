class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i = 0
        minPrefix = []
        currMin = float("inf")
        for i in nums[::-1]:
            currMin = min(currMin, i)
            minPrefix.append(currMin)
        minPrefix.reverse()
        for i in range(len(nums)):
            if nums[i] != minPrefix[i]:
                break
            else:
                i += 1
        if i == len(nums):
            return 0

        j = 0
        maxPrefix = []
        currMax = -float("inf")
        for j in nums:
            currMax = max(currMax, j)
            maxPrefix.append(currMax)
        
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] != maxPrefix[j]:
                break
        return j - i + 1