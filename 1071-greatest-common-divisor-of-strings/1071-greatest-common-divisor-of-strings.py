class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        maxLen = gcd(len(str1), len(str2))
        ans = ''
        compareStr = ''
        for i in range(0, maxLen):
            compareStr += str1[i]
            compareStr1 = compareStr * (len(str1) // (i + 1))
            compareStr2 = compareStr * (len(str2) // (i + 1))
            if compareStr2 == str2 and compareStr1 == str1:
                ans = compareStr
        return ans