class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        selected = 0
        ways = 0
        if nums[0]:
            ways += 1
        for i in range(len(nums)):
            selected += 1
            if selected > nums[i] and (i == len(nums) - 1 or nums[i + 1] > selected):
                ways += 1
        return ways