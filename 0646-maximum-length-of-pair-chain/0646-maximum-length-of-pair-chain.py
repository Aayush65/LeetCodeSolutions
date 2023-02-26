class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()

        memo = {}
        def dp(index: int) -> int:
            if index in memo:
                return memo[index]
            res = 0
            for i in range(index + 1, len(pairs)):
                if pairs[index][1] < pairs[i][0]:
                    res = max(res, dp(i))
            res += 1
            memo[index] = res
            return res
            
        return max([dp(i) for i in range(len(pairs))])