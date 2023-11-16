class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = ''
        for i in range(len(nums)):
            if nums[i][i] == '1':
                s += '0'
            else:
                s += '1'
        return s