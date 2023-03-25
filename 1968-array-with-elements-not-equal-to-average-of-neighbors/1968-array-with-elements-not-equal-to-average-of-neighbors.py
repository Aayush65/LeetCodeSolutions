class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0] * len(nums)
        median = nums[len(nums) // 2] if len(nums) % 2 else (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2
        for i in range(ceil(len(nums) / 2)):
            res[i * 2] = nums[i]
        for i in range(len(nums) // 2):
            res[i * 2 + 1] = nums[i + ceil(len(nums) / 2)]
        return res