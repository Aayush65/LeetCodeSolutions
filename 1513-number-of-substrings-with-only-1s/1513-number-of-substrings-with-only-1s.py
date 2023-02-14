class Solution:
    def numSub(self, s: str) -> int:
        mod = 1000000007
        i = 0
        subStrs = 0
        while i < len(s):
            if s[i] == '0':
                i += 1
                continue
            count = 0
            while i < len(s) and s[i] == '1':
                count += 1
                i += 1
            subStrs += (count * (count + 1) // 2) % mod
        return subStrs % mod