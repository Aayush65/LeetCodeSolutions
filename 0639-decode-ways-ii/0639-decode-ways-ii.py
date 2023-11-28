class Solution:
    def numDecodings(self, s: str) -> int:
        mod = int(1e9 + 7)
        
        @cache
        def dp(index: int) -> int:
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            res = dp(index + 1)
            if s[index] == '*':
                res *= 9
            if index + 1 < len(s):
                if s[index] == '*':
                    if s[index + 1] == '*':
                        res += 15 * dp(index + 2)
                    elif -1 < int(s[index + 1]) < 7:
                        res += 2 * dp(index + 2)
                    else:
                        res += dp(index + 2)
                elif int(s[index]) == 1:
                    if s[index + 1] == '*':
                        res += 9 * dp(index + 2)
                    else:
                        res += dp(index + 2)
                elif int(s[index]) == 2:
                    if s[index + 1] == '*':
                        res += 6 * dp(index + 2)
                    elif -1 < int(s[index + 1]) < 7:
                        res += dp(index + 2)
            res %= mod
            return res
        
        return dp(0)
            