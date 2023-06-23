class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        n = len(arr)
        eleMap = {i: [] for i in arr}
        for i in range(len(arr)):
            eleMap[arr[i]].append(i)
            
        @cache
        def dp(index: int) -> int:
            if index == n:
                return 0
            length = 1
            nextEle = arr[index] + diff
            if nextEle in eleMap:
                idx = bisect_left(eleMap[nextEle], index + 1)
                if idx < len(eleMap[nextEle]):
                    length += dp(eleMap[nextEle][idx])
            return length
        
        maxLen = 0
        for i in range(n):
            maxLen = max(maxLen, dp(i))
        return maxLen