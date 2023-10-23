class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def finalStr(s: str) -> str:
            stack = []
            for i in s:
                if i == '#':
                    if stack: stack.pop()
                else:
                    stack.append(i)
            print(stack)
            return ''.join(stack)
        
        return finalStr(s) == finalStr(t)