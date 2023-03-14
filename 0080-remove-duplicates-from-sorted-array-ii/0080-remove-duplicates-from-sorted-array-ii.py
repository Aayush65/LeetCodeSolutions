class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hm = {i: 0 for i in nums}
        for i in nums:
            hm[i] += 1
        
        for i in range(len(nums) - 1, -1, -1):
            if hm[nums[i]] > 2:
                hm[nums[i]] -= 1
                nums[i] = 100001
        
        while nums[-1] == 100001:
            nums.pop()
        j = 0
        for i in range(len(nums)):
            while j < i and nums[j] != 100001:
                j += 1
            if nums[i] != 100001 and nums[j] == 100001:
                nums[j] = nums[i]
                nums[i] = 100001
        return j + 1