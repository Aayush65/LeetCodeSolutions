class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pushed.reverse()
        popped.reverse()
        while pushed or popped:
            if stack and popped and popped[-1] == stack[-1]:
                stack.pop()
                popped.pop()
                continue
            elif pushed:
                stack.append(pushed.pop())
            else:
                return False
        return True
        