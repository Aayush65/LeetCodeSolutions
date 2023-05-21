class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        @cache
        def dfs(i, cur_sum):
            if i==n:
                return 1
            
            skip = dfs(i+1, cur_sum)
            include = 0
            if nums[i] + cur_sum < k:
                include = dfs(i+1, cur_sum + nums[i])
                
            return skip + include
        
        less_than_k = 2 * dfs(0,0)
        return max(2**n - less_than_k, 0) % (10**9 + 7)