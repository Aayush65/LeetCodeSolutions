class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        preSum = [0]
        for i in stoneValue:
            preSum.append(preSum[-1] + i)

        memo = [-float("inf")] * len(stoneValue)
        def dp(index: int) -> int:
            if index == len(stoneValue):
                return 0
            if memo[index] != -float("inf"):
                return memo[index]
            stones = 0
            res = -float("inf")
            for i in range(index, min(len(stoneValue), index + 3)):
                stones += stoneValue[i]
                otherPlayer = dp(i + 1)
                score = preSum[-1] - preSum[i + 1] - otherPlayer
                res = max(res, score + stones)
            memo[index] = res
            return res

        alice = dp(0)
        if alice == preSum[-1] / 2:
            return "Tie"
        return "Alice" if alice > preSum[-1] / 2 else "Bob"