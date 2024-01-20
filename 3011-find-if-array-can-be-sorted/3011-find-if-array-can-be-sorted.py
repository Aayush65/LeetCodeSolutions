class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        countBits = lambda x: bin(x).count('1')
        newArr = []
        i = 0
        while i < len(nums):
            j = i
            currArr = []
            while j < len(nums) and countBits(nums[j]) == countBits(nums[i]):
                currArr.append(nums[j])
                j += 1
            i = j
            newArr.extend(sorted(currArr))
        
        for i in range(1, len(newArr)):
            if newArr[i] < newArr[i - 1]:
                return False
        return True