class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        n = len(set(nums))
        if n == 3:
            return "scalene"
        if n == 2:
            return "isosceles"
        return "equilateral"