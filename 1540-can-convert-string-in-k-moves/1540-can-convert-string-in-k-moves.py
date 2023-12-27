class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        requirements = [0] * 26
        for i, j in zip(s, t):
            diff = (ord(j) - ord(i)) % 26
            requirements[diff] += 1
        
        for i in range(1, 26):
            chances = k // 26
            if i and i <= k % 26:
                chances += 1
            if chances < requirements[i]:
                return False
        return True