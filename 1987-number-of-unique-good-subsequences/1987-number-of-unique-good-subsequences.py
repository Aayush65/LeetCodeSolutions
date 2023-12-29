class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = int(1e9 + 7)
        
        @cache
        def dp(index: int, prev: int) -> int:
            if index == len(binary):
                return 1
            res = dp(index + 1, binary[index])
            if binary[index] != prev:
                res += dp(index + 1, prev)
            res %= mod
            return res
            
        res = 0
        isZeroExist = 0
        for i, x in enumerate(binary):
            if x == '1':
                res += dp(i + 1, '1')
            else:
                isZeroExist = 1
            res %= mod
        return res + isZeroExist
    