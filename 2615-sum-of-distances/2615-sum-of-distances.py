class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hm = {i: [] for i in nums}

        res = [0] * len(nums)
        for i in range(len(nums)):
            score =  0
            if hm[nums[i]]:
                sc, count, idx = hm[nums[i]]
                score = sc + count * (i - idx)
                hm[nums[i]] = [score, count + 1, i]
            else:
                hm[nums[i]] = [0, 1, i] 
            res[i] += score
        nums.reverse()
        
        hm = {i: [] for i in nums}
        for i in range(len(nums)):
            score =  0
            if hm[nums[i]]:
                sc, count, idx = hm[nums[i]]
                score = sc + count * (i - idx)
                hm[nums[i]] = [score, count + 1, i]
            else:
                hm[nums[i]] = [0, 1, i] 
            res[-i - 1] += score
        return res