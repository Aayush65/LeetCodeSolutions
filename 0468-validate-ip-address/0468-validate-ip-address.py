class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(s: str) -> bool:
            eles = s.split('.')
            validEles = {'1','2','3','4','5','6','7','8','9','0'}
            if len(eles) != 4:
                return False
            for i in eles:
                for j in i:
                    if j not in validEles:
                        return False 
                if not (i and 0 <= int(i) <= 255 and i == str(int(i))): 
                    return False
            return True

        def isIPv6(s: str) -> bool:
            eles = s.split(':')
            validEles = {'1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','a','b','c','d','e','f'}
            if len(eles) != 8:
                return False
            for i in eles:
                if not 1 <= len(i) <= 4:
                    return False
                for j in i:
                    if j not in validEles:
                        return False
            return True
        
        if isIPv4(queryIP):
            return "IPv4"
        elif isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"