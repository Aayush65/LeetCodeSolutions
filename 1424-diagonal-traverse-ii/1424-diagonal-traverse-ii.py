class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m, n = len(nums), max(len(row) for row in nums)
        diags = [[] for _ in range(m + n)]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diags[i + j].append(nums[i][j])
        res = []
        for i in diags:
            res.extend(i[::-1])
        return res