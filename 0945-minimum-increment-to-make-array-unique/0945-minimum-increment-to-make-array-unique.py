class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        hm = {i: 0 for i in nums}
        for i in nums:
            hm[i] += 1
        nums.sort()
        
        ops = 0
        curr = min(nums)
        for i in nums:
            if hm[i] > 1:
                hm[i] -= 1
                while curr in hm or curr <= i:
                    curr += 1
                hm[curr] = 1
                ops += curr - i
        return ops
        