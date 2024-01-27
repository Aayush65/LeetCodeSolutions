class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
        mod = int(1e9 + 7)
        
        # O(n * n * k) TC
        
#         @cache
#         def dp(index: int, k: int) -> int:
#             if k == 0:
#                 return 1
#             res = 0
#             for i in range(n - index):
#                 if i > k:
#                     break
#                 res += dp(index + 1, k - i)
#                 res %= mod
#             return res
            
#         return dp(0, k)

        k += 1
        curr = [0] * k
        curr[0] = 1

        for i in range(n):
            last = curr
            curr = [0] * k
            currSum = 0
            for j in range(k):
                currSum += last[j]
                if j - i - 1 > -1:
                    currSum -= last[j - i - 1]
                currSum %= mod
                curr[j] = currSum
        return curr[-1]