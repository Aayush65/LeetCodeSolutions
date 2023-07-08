class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        
        @cache
        def dp(index: int) -> int:
            if index == len(s):
                return 0
            if s[index] == '0':
                return float("inf")
            currNum = ''
            res = float("inf")
            for i in range(index, len(s)):
                currNum += s[i]
                num = int(currNum, 2)
                logVal = log(num, 5)
                if logVal - int(logVal) <= 10 ** -5:
                    res = min(res, 1 + dp(i + 1))
            return res
            
            
        res = dp(0)
        return -1 if res == float("inf") else res