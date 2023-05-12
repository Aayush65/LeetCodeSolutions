class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stoneMap = {stones[i]: i for i in range(len(stones))}
        
        @cache
        def dp(index: int, lastJump: int) -> bool:
            if index == len(stones) - 1:
                return True
            if lastJump > 1 and stones[index] + lastJump - 1 in stoneMap and dp(stoneMap[stones[index] + lastJump - 1], lastJump - 1):
                return True
            if lastJump and stones[index] + lastJump in stoneMap and dp(stoneMap[stones[index] + lastJump], lastJump):
                return True
            if stones[index] + lastJump + 1 in stoneMap and dp(stoneMap[stones[index] + lastJump + 1], lastJump + 1):
                return True
            return False
            
        return dp(0, 0)