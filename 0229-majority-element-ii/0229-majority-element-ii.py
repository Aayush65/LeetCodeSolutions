class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0    
            hashmap[i] += 1
            if len(hashmap) > 2:
                keys = [j for j in hashmap]
                for j in keys:
                    hashmap[j] -= 1
                    if not hashmap[j]:
                        del hashmap[j]
        
        count = {i: 0 for i in hashmap}
        for i in nums:
            if i in hashmap:
                count[i] += 1
                
        res = []
        for i in hashmap:
            if count[i] > len(nums) / 3:
                res.append(i)
        return res
            