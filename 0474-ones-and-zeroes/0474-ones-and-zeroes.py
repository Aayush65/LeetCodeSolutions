class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        nums = []
        for s in strs:
            count = 0
            for i in s:
                if i == '0':
                    count += 1
            nums.append((count, len(s) - count))
        
        @cache
        def dp(index: int, m: int, n: int) -> int:
            if m < 0 or n < 0:
                return -1
            if index == len(nums) or (m == 0 and n == 0):
                return 0
            take = 1 + dp(index + 1, m - nums[index][0], n - nums[index][1])
            notTake = dp(index + 1, m, n)
            return max(take, notTake)            
            
        return dp(0, m, n)