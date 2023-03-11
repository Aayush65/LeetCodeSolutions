class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        leftOnes = [0]
        rightOnes = [0]
        for i in nums:
            if i == 1:
                leftOnes.append(leftOnes[-1] + 1)
            else:
                leftOnes.append(0)
        for i in nums[::-1]:
            if i == 1:
                rightOnes.append(rightOnes[-1] + 1)
            else:
                rightOnes.append(0)
        rightOnes.reverse()
        
        maxLen = 0
        for i in range(len(nums)):
            maxLen = max(maxLen, leftOnes[i] + rightOnes[i + 1])
        return maxLen