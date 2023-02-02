class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        i = len(nums) - 1
        maxSteps = 0
        while i > -1:
            steps = 0
            while stack and stack[-1][0] < nums[i]:
                steps = max(1 + steps, stack.pop()[1])
            stack.append([nums[i], steps])
            i -= 1
            maxSteps = max(maxSteps, steps)
        return maxSteps