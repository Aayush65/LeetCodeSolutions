class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        curr = nums[0]
        for i in nums:
            if count == 0:
                curr = i
            count += 1 if curr == i else -1
        return curr