class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in brackets:
                if not stack or stack.pop() != brackets[i]:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0