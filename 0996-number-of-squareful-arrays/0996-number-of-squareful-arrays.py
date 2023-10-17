class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
                
        def dp(num: int, nums: list[int]) -> int:
            nums.remove(num)
            if not nums:
                return 1
            res = 0
            for i in set(nums):
                sqrt = (i + num) ** 0.5
                if sqrt == int(sqrt):
                    res += dp(i, nums.copy())
            return res
            
        return sum(dp(i, nums.copy()) for i in set(nums))