class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        preXOR = []
        currXOR = 0
        for i in nums:
            currXOR ^= i
            preXOR.append(currXOR)
        
        hm = defaultdict(int)
        for i in preXOR:
            hm[i] += 1
        
        count = 0
        for i in preXOR:
            if i == 0:
                count += 1
            hm[i] -= 1
            count += hm[i]
        return count