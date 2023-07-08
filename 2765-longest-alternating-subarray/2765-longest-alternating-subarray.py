class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        maxLength = 0
        for i in range(len(nums) - 1):
            alternating = True
            n1, n2 = nums[i], nums[i + 1]
            if n2 != n1 + 1:
                continue
            length = 2
            for j in range(i + 2, len(nums)):
                if alternating and nums[j] != n1:
                    break
                if not alternating and nums[j] != n2:
                    break
                alternating = not alternating
                length += 1
            maxLength = max(maxLength, length)
        return maxLength if maxLength > 1 else -1
