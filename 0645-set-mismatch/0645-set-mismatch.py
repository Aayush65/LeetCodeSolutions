class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashset = set()
        repeated = nums[0]
        total = 0
        for i in nums:
            if i in hashset:
                repeated = i
            hashset.add(i)
            total += i
        replaced = len(nums)*(len(nums)+1)//2 + repeated - total
        return [repeated, replaced]