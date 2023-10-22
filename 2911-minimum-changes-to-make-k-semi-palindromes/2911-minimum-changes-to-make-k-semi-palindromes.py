class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        
        @cache
        def semiPalindromeCost(i: int, j: int, k: int) -> int: 
            cost = 0
            n = j - i + 1
            for x in range(k):
                newS = []
                for y in range(n // k):
                    newS.append(s[i + x + y * k])
                for y in range(len(newS) // 2):
                    if newS[y] != newS[- y - 1]:
                        cost += 1
            return cost                 

        @cache
        def palindromeCost(i: int, j: int) -> int:
            minCost = float("inf")
            n = j - i + 1
            for k in range(1, n):
                if n % k == 0:
                    minCost = min(minCost, semiPalindromeCost(i, j, k))
            return minCost

        n = len(s)

        @cache
        def dp(index: int, k: int) -> int:
            if k == 0 and index == n:
                return 0
            if k == 0 or index == n:
                return float("inf")
            res = float("inf")
            for i in range(index + 1, n):
                # print(s[index: i + 1], palindromeCost(index, i))
                res = min(res, palindromeCost(index, i) + dp(i + 1, k - 1))
            return res

        res = dp(0, k)
        return -1 if res == float("inf") else res