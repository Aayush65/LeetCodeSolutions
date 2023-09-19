class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while True:
            while nums[i] == i + 1:
                i += 1
            if nums[i] == nums[nums[i] - 1]:
                break
            next_index = nums[i] - 1
            nums[i], nums[next_index] = nums[next_index], nums[i]
        return nums[i]