class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        # memo = {}
        # def dp(l: int, r: int) -> int:
        #     if (l, r) in memo:
        #         return memo[(l, r)]
        #     key = (l, r)
        #     while l < r and s[l] == 'a':
        #         l += 1
        #     while r > l and s[r] == 'b':
        #         r -= 1
        #     if l == r:
        #         return 0
        #     res = 1 + min(dp(l + 1, r), dp(l, r - 1))
        #     memo[key] = res
        #     return res
            
        # return dp(0, len(s) - 1)

        rightA = [0]
        for i in s[::-1]:
            if i == 'a':
                rightA.append(rightA[-1] + 1)
            else:
                rightA.append(rightA[-1])
        rightA.reverse()
        minOps = len(s)
        currA = 0
        for i in range(len(s) + 1):
            ops = rightA[i] + i - currA
            if i < len(s) and s[i] == 'a':
                currA += 1
            minOps = min(minOps, ops)
        return minOps
