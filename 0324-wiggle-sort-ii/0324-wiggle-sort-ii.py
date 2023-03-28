class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        res = [0] * len(nums)
        median = nums[len(nums) // 2] if len(nums) % 2 else (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2        
        evens = [nums[i] for i in range(ceil(len(nums) / 2))]
        odds = [nums[i] for i in range(ceil(len(nums) / 2), len(nums))]
        # print(evens)
        # print(odds)
        evens.reverse()
        odds.reverse()
        for i in range(len(nums)):
            if i % 2:
                nums[i] = odds[i // 2]
            else:
                nums[i] = evens[i // 2]
        return nums