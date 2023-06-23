class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        indexMap = {i: [] for i in nums}
        for i in range(n):
            indexMap[nums[i]].append(i)
        
        @cache
        def dp(index: int, diff: int) -> int:
            if index == n:
                return 0
            length = 1
            nextEle = nums[index] + diff
            if nextEle in indexMap:
                idx = bisect_left(indexMap[nextEle], index + 1)
                if idx < len(indexMap[nextEle]):
                    length += dp(indexMap[nextEle][idx], diff)
            return length
            
        
        maxLen = 1
        for i in range(n):
            for j in range(i + 1, n):
                maxLen = max(maxLen, 1 + dp(j, nums[j] - nums[i]))
        return maxLen