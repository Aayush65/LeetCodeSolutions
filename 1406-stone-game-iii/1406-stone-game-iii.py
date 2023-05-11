class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        preSum = [0]
        for i in stoneValue:
            preSum.append(preSum[-1] + i)
            
        @cache
        def dp(index: int) -> int:
            if index == len(stoneValue):
                return 0
            stones = 0
            res = -float("inf")
            for i in range(index, min(len(stoneValue), index + 3)):
                stones += stoneValue[i]
                otherPlayer = dp(i + 1)
                score = preSum[-1] - preSum[i + 1] - otherPlayer
                res = max(res, score + stones)
            return res
            
        alice = dp(0)
        if alice == preSum[-1] / 2:
            return "Tie"
        return "Alice" if alice > preSum[-1] / 2 else "Bob"