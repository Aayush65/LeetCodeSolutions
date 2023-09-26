class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []

        ifInStack = [False]*26
        lastIndex = [0]*26

        index = lambda i : ord(i) - ord('a')

        for x, i in enumerate(s):
            lastIndex[index(i)] = x

        for x, i in enumerate(s):
            if not ifInStack[index(i)]:
                while stack and i < stack[-1] and lastIndex[index(stack[-1])] > x:      # (1)
                    ifInStack[index(stack[-1])] = False
                    stack.pop()
                stack.append(i)
                ifInStack[index(i)] = True

        s1 = ''.join(stack)
        return s1 