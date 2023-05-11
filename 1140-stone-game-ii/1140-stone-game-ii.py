class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        preSum = [0]
        for i in piles:
            preSum.append(preSum[-1] + i)
                
        @cache
        def dp(index: int, canTake: int) -> int:
            if index == len(piles):
                return 0
            res = 0
            stones = 0
            for i in range(index, min(len(piles), index + 2 * canTake)):
                stones += piles[i]
                diffPlayer = dp(i + 1, max(canTake, i - index + 1))
                score = preSum[-1] - preSum[i + 1] - diffPlayer
                res = max(res, stones + score)
            return res
        
        return dp(0, 1)