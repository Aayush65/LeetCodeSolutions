class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        maxLen = 0
        
        length = 0
        minus = 0
        for i in nums:
            if not i:
                length = 0
                minus = 0
                continue
            if i < 0:
                minus += 1
            length += 1
            if minus % 2 == 0:
                maxLen = max(maxLen, length)
        
        length = 0
        minus = 0
        for i in nums[::-1]:
            if not i:
                length = 0
                minus = 0
                continue
            if i < 0:
                minus += 1
            length += 1
            if minus % 2 == 0:
                maxLen = max(maxLen, length)
        
        return maxLen