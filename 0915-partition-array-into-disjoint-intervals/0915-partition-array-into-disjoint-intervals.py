class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxArr = []
        mx = nums[0]
        for i in nums:
            mx = max(mx, i)
            maxArr.append(mx)
        
        minArr = []
        mn = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            mn = min(mn, nums[i])
            minArr.append(mn)
        minArr.reverse()

        for i in range(len(nums) - 1):
            if maxArr[i] <= minArr[i + 1]:
                return i + 1