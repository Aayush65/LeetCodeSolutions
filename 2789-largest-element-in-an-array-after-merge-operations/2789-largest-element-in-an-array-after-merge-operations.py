class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        nums.reverse()
        stack = []
        for i in nums:
            while stack and stack[-1] >= i:
                i += stack.pop()
            stack.append(i)
        return max(stack)