class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        allRes = []
        s = list(s)
        
        def backtracking(index: int):
            if index == len(s):
                allRes.append(''.join(s))
                return
            if ord(s[index]) > 64:
                if ord(s[index]) < 96:
                    s[index] = chr(ord(s[index]) + 32)
                    backtracking(index + 1)
                    s[index] = chr(ord(s[index]) - 32)
                else:
                    s[index] = chr(ord(s[index]) - 32)
                    backtracking(index + 1)
                    s[index] = chr(ord(s[index]) + 32)
            backtracking(index + 1)
        
        backtracking(0)
        return allRes
            