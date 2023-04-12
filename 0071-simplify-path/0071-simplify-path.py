class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        currDir = []
        for i, s in enumerate(path):
            if stack and stack[-1] == '/' and s == '/':
                continue
            if s != '/':
                currDir.append(s)
            if s == '/' or i == len(path) - 1:
                currDirStr = ''.join(currDir)
                if currDirStr == '.':
                    while stack and stack[-1] != '/':
                        stack.pop()
                elif currDirStr == '..':
                    oneSlash = True
                    while stack and (stack[-1] != '/' or oneSlash):
                        if len(stack) == 1 or stack.pop() == '/':
                            oneSlash = False
                else:
                    stack.append(s)
                currDir = []
            else:
                stack.append(s)
        if len(stack) > 1 and stack[-1] == '/':    
            stack.pop()
        return ''.join(stack) if stack else '/'