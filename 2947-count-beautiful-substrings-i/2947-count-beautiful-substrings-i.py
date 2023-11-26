class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        count = 0
        n = len(s)
        
        for i in range(n):
            v, c = 0, 0    
            for j in range(i, n):
                if s[j] in vowels:
                    v += 1
                else:
                    c += 1
                if v == c and (v * c) % k == 0:
                    count += 1
        return count