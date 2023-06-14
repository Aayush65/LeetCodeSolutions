class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            nums.sort()
            numsMap = {i: 0 for i in nums}
            pairs = 0
            for i in nums:
                numsMap[i] += 1
                if numsMap[i] == 2:
                    pairs += 1
            return pairs
        
        nums = list(set(nums))
        nums.sort()
        
        numsMap = set(nums)
            
        pairs = 0
        for i in nums:
            if i + k in numsMap:
                pairs += 1
        return pairs