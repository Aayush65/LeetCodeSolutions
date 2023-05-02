class Solution:
    def arraySign(self, nums: List[int]) -> int:
        minus = 0
        for i in nums:
            if i:
                if i < 0:
                    minus += 1
            else:
                return 0
        return -1 if minus % 2 else 1