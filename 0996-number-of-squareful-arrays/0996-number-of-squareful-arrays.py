class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        nums.sort()        
        
        memo = {}
        def dp(num: int, nums: list[int]) -> int:
            if (num, tuple(nums)) in memo:
                return memo[(num, tuple(nums))]
            nums.remove(num)
            if not nums:
                return 1
            res = 0
            for i in set(nums):
                sqrt = (i + num) ** 0.5
                if sqrt == int(sqrt):
                    res += dp(i, nums.copy())
                                
            # memo[(num, tuple(nums))] = res
            return res
            
        return sum(dp(i, nums.copy()) for i in set(nums))