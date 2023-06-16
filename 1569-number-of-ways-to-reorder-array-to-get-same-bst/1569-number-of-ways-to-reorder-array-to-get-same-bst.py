class Solution:
    
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 1000000007
        memo = {}

        def innerRec(nums: list[int]) -> int:
            n = len(nums)
            if n <= 2:
                return 1
            if tuple(nums) in memo:
                return memo[tuple(nums)]

            left, right = [], []
            for i in nums:
                if i < nums[0]:
                    left.append(i)
                elif i > nums[0]:
                    right.append(i - nums[0])

            leftWays = innerRec(left)
            rightWays = innerRec(right)

            combinations = comb(len(left) + len(right), len(left)) % MOD
            combinations = (combinations * leftWays) % MOD
            combinations = (combinations * rightWays) % MOD

            memo[tuple(nums)] = combinations
            return combinations

        return innerRec(nums) - 1