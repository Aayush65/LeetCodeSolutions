class Solution:
    def smallestString(self, s: str) -> str:
        s = list(s)
        if set(s) == {'a'}:
            s[len(s) - 1] = 'z'
            return ''.join(s)
        
        aIdxStart, aIdxEnd = 0, len(s)
        while s[aIdxStart] == 'a':
            aIdxStart += 1
            
        for i in range(aIdxStart, len(s)):
            if s[i] == 'a':
                aIdxEnd = i
                break
                
        def stepBack(l: int, r: int) -> None:
            for i in range(l, r):
                if s[i] == 'a':
                    continue
                s[i] = chr(ord(s[i]) - 1)
        
        
        stepBack(aIdxStart, aIdxEnd)
        return ''.join(s)