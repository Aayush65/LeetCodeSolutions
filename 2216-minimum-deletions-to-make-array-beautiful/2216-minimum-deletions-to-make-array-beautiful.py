class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            if len(stack) % 2:
                if stack[-1] != nums[i]:
                    stack.append(nums[i])
            else:
                stack.append(nums[i])
        print(stack)
        return len(nums) - len(stack) + (len(stack) % 2)