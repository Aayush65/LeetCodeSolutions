class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def factors(n: int) -> list[int]:
            res = []
            for i in range(1, n):
                if n % i == 0:
                    res.append(i)
            return res
            
        allFactors = factors(len(s))[::-1]
        for i in allFactors:
            if s[:i] * (len(s) // i) == s:
                return True
        return False