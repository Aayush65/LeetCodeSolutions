class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        evenPool, oddPool = {}, {}
        for i in range(len(s1)):
            if i % 2:
                if s1[i] not in oddPool:
                    oddPool[s1[i]] = 0
                oddPool[s1[i]] += 1
            else:
                if s1[i] not in evenPool:
                    evenPool[s1[i]] = 0
                evenPool[s1[i]] += 1
                
        for i in range(len(s2)):
            if i % 2:
                if s2[i] in oddPool and oddPool[s2[i]]:
                    oddPool[s2[i]] -= 1
                else:
                    return False
            else:
                if s2[i] in evenPool and evenPool[s2[i]]:
                    evenPool[s2[i]] -= 1
                else:
                    return False
        
        for i in evenPool:
            if evenPool[i]:
                return False
            
        for i in oddPool:
            if oddPool[i]:
                return False
        
        return True