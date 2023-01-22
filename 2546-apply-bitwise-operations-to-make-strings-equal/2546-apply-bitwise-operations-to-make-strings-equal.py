class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if int(target) == 0 or int(s) == 0:
            for i in range(len(s)):
                if target[i] != s[i]:
                    return False
            return True
        return True
                
                