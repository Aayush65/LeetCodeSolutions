class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            rightCut = bisect_left(nums, target - nums[i])
            if rightCut <= i:
                break
            count += rightCut - i - 1
        return count