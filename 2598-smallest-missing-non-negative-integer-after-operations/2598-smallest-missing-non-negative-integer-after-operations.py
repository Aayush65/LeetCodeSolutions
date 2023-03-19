class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        for i in range(len(nums)):
            nums[i] %= value
        hm = {i: 0 for i in nums}
        for i in nums:
            hm[i] += 1
        mex = 0
        while True:
            if mex % value in hm and hm[mex % value]:
                hm[mex % value] -= 1
                mex += 1
            else:
                return mex  