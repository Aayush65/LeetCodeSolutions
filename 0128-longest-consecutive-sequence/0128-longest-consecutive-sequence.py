class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        hashmap = {}
        for i in nums:
            if i - 1 not in numSet:
                hashmap[i] = 0

        maxLen = 0
        for i in hashmap:
            root = i
            while i in numSet:
                hashmap[root] += 1
                i += 1
            maxLen = max(maxLen, hashmap[root])
    
        return maxLen