class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        primes = {'2','3','5','7'}
        mod = 1000000007

        if s[0] not in primes or s[-1] in primes:
            return 0

        dividers = [0]
        for i in range(len(s) - 1):
            if s[i] not in primes and s[i + 1] in primes:
                dividers.append(i + 1)

        @cache
        def dp(index: int, k: int) -> int:
            if k == 0:
                if len(s) - dividers[index] >= minLength:
                    return 1
                return 0
            res = 0
            for i in range(index + 1, len(dividers) - k + 1):
                if dividers[i] - dividers[index] >= minLength:
                    res += dp(i, k - 1)
            return res % mod

        return dp(0, k - 1)