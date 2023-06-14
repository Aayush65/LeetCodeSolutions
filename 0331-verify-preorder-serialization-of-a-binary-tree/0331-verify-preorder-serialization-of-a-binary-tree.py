class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        nodes = preorder.split(',')
        for i in nodes:
            stack.append(i)
            while len(stack) > 2 and stack[-1] == '#' and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                if stack.pop() == '#':
                    return False
                stack.append('#')
        return len(stack) == 1 and stack[-1] == '#'