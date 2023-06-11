class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) > 2 and stack[-3:] == ['a','b','c']:
                stack.pop()
                stack.pop()
                stack.pop()
        return len(stack) == 0